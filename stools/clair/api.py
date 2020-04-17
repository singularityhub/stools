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


import requests
import os
import sys


class Clair(object):
    """the ClairOS security scanner to scan Docker layers"""

    def __init__(self, host, port, api_version="v1"):

        if not host.startswith("http"):
            host = "http://%s" % host

        self.url = "%s:%s/%s" % (host, port, api_version)

    def __str__(self):
        return "Clair URL: %s" % self.url

    def __repr__(self):
        return self.__str__()

    def scan(self, targz_url, name):
        url = os.path.join(self.url, "layers")

        data = {"Name": name, "Path": targz_url, "Parentname": "", "Format": "Docker"}

        response = requests.post(url, json={"Layer": data})

        if response.status_code != 201:
            print("Error creating %s at %s" % (data["Path"], url))
            sys.exit(1)

    def report(self, name):
        """generate a report for an image of interest. The name should
           correspond to the same name used when adding the layer...

           Parameters
           ==========
        """

        url = os.path.join(self.url, "layers", name)
        response = requests.get(url, params={"features": True, "vulnerabilities": True})
        if response.status_code == 200:
            return response.json()
        else:
            print("Error with %s" % url)
            sys.exit(1)

    def ping(self):
        """ping serves as a health check. If healthy, will return True.
           We do this because the user is starting Clair as
           a separate (Docker) image and it might be the case that the
           server port/host are not correctly set.

           Returns
           =======
           healthy: If healthy, returns True, otherwise False

        """
        url = os.path.join(self.url, "namespaces")
        response = requests.get(url)

        try:
            if response.status_code != 200:
                return False
            namespaces = response.json()["Namespaces"]
            print("Found %s Clair namespaces" % len(namespaces))
            return True
        except:
            print("Cannot find Clair running at %s" % url)
        return False

    def print(self, report):
        """print the report items"""

        if "Features" in report["Layer"]:
            items = report["Layer"]["Features"]

            for item in items:
                if "Vulnerabilities" in item:
                    print("%s - %s" % (item["Name"], item["Version"]))
                    print("-" * len(item["Name"] + " - " + item["Version"]))
                    for v in item["Vulnerabilities"]:
                        print(v["Name"] + " (" + v["Severity"] + ")")
                        print(v["Link"])
                        print(v["Description"])
                        print("\n")
        else:
            print("%s does not have any vulnerabilities!" % report["Layer"]["Name"])
