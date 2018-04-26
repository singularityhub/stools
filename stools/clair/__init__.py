#!/usr/bin/env python

'''

Copyright (C) 2018 The Board of Trustees of the Leland Stanford Junior
University.
Copyright (C) 2018 Vanessa Sochat.

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

'''

from stools.version import __version__
from stools.clair.image import export_to_targz
import argparse
import tempfile
import sys
import os


def get_parser():
    parser = argparse.ArgumentParser(description="Singularity Clair Scanner")

    parser.add_argument('--version', dest="version", 
                        help="show version and exit.", 
                        default=False, action='store_true')

    parser.add_argument("images", nargs='*',
                         help='Singularity images to scan.', 
                         type=str)

    parser.add_argument("--port", default=8080,
                      help='port to serve application (default 8080)', 
                      type=int)

    parser.add_argument("--host", default="127.0.0.1",
                         help='host to serve application (default 127.0.0.1)', 
                         type=str)

    return parser

def version():
    print("\nSingularity Clair Scanner v%s" %__version__)


def main():

    parser = get_parser()

    def help(retval=0):
        '''print help, including the software version and active client 
           and exit with return code.
        '''
        version()
        parser.print_help()
        sys.exit(retval)
    

    # If the user didn't provide any arguments, show the full help
    if len(sys.argv) == 1:
        help()
    try:
        args = parser.parse_args()
    except:
        sys.exit(0)

    if args.version is True:
        version()
        sys.exit(0)

    print(args.images)

    # 2. Start server for images
    # UNDER DEVELOPMENT!

    webroot = tempfile.mkdtemp()

    # Start the server and serve static files from root
    from stools.clair.server import start

    start(port=args.port, host=args.host, static_folder=webroot)


    for image in images:

        # 1. decompress to sandbox --> tar.gz
        targz = export_to_targz(image)


if __name__ == '__main__':
    main()
