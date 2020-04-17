#!/usr/bin/env python

"""

Copyright (C) 2018-2019 Vanessa Sochat.

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or (at your
option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public
License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""

import argparse
import json
import shutil
import sys
from multiprocessing import Process
from os import rename
from os.path import isdir, join, basename, splitext
from time import sleep

import requests
from json2html import *
from lxml import etree, html

from stools.clair.api import Clair
from stools.clair.image import export_to_targz
from stools.clair.server import start
from stools.version import __version__


def get_parser():
    parser = argparse.ArgumentParser(prog="Singularity Clair Scanner", usage=usage())

    parser.add_argument(
        "--version",
        action="version",
        version=version(),
        dest="version",
        help="show version and exit",
        default=False,
    )

    parser.add_argument(
        "--start-server",
        dest="server",
        help="if running natively, start the web server too",
        default=True,
        action="store_true",
    )

    parser.add_argument(
        "images", nargs="*", help="Singularity images to scan", type=str
    )

    parser.add_argument(
        "--port",
        default=8080,
        help="port to serve application (default 8080)",
        type=int,
    )

    parser.add_argument(
        "--report",
        nargs="?",
        const="/code/reports",
        help="save Clair reports to chosen directory (default: /code/reports)",
        type=dir_path,
    )

    parser.add_argument(
        "--report-format",
        choices=["json", "html"],
        default="json",
        dest="report_format",
        help="reports will be saved in specified format when --report passed (default: json)",
        type=str,
    )

    parser.add_argument(
        "--host",
        default="0.0.0.0",
        help="host to serve application (default 0.0.0.0)",
        type=str,
    )

    parser.add_argument(
        "--clair-port",
        default=6060,
        help="port Clair is running on (default 6060)",
        type=int,
        dest="clair_port",
    )

    parser.add_argument(
        "--clair-host",
        default="0.0.0.0",
        help="host Clair is running on (default clair-scanner)",
        type=str,
        dest="clair_host",
    )

    return parser


def dir_path(string):
    if isdir(string):
        return string
    else:
        print("%s is not a directory" % string)
        sys.exit(0)


def usage():
    return """sclair [images] [options]"""


def version():
    print("\nSingularity Clair Scanner v%s" % __version__)


def main():
    parser = get_parser()

    # If the user didn't provide any arguments, show the full help
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(0)
    try:
        args = parser.parse_args()
    except:
        sys.exit(0)

    if args.version is True:
        version()
        sys.exit(0)

    if args.report is None and args.report_format is not None:
        print("\nWarning: --report-format has no effect when --report is not passed\n")

    # Generate Clair controller
    clair = Clair(args.clair_host, args.clair_port)
    if not clair.ping():
        sys.exit(1)

    print(clair)

    # Local Server
    webroot = "/var/www/images"

    # Start the server and serve static files from root
    if args.server is True:
        print("\n1. Starting server...")
        server = "http://%s:%s/" % (args.host, args.port)
        process = Process(target=start, args=(args.port, args.host, webroot))
        process.daemon = True
        process.start()
        sleep(1)

    # Check health of clair server
    print("\n1. Checking server...")
    response = requests.get(server)
    if response.status_code != 200:
        print("Server not found running at %s" % server)
        sys.exit(1)

    print("2. Processing images!")
    for image in args.images:

        # 1. decompress to sandbox --> tar.gz
        targz = export_to_targz(image)
        print("...exported %s to %s" % (image, targz))

        # 2. Move to webroot
        targz_web = join(webroot, basename(targz))
        rename(targz, targz_web)
        targz_url = "%simages/%s" % (server, basename(targz))

        # 3. Scan with Clair, use image name
        print("...serving %s to Clair" % targz_url)
        clair.scan(targz_web, basename(image))

        # 4. Generate report
        print("3. Generating report!")
        report = clair.report(basename(image))
        if args.report is not None:
            fname = splitext(basename(image))[0] + ".%s" % args.report_format
            fpath = join(args.report, fname)
            if args.report_format == "json":
                fmtreport = json.dumps(report, indent=4)
            elif args.report_format == "html":
                htmlreport = (
                    """<html><head><title>Vulnerability Report</title></head><h2 align="center">%s Vulnerability Report</h2><body><div align="center">%s</div></body></html>"""
                    % (image, json2html.convert(json=report))
                )
                fmtreport = etree.tostring(
                    html.fromstring(htmlreport), encoding="unicode", pretty_print=False
                )
            with open(fpath, "w+") as file:
                file.write(fmtreport)
            print("Wrote report to %s" % fpath)
        else:
            clair.print(report)

    # Shut down temporary server
    process.terminate()
    shutil.rmtree(webroot)


if __name__ == "__main__":
    main()
