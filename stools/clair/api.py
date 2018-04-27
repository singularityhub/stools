'''

Copyright (c) 2018, Vanessa Sochat
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

'''


import requests
import os
import sys


class Clair(object):
    '''the ClairOS security scanner to scan Docker layers'''

    def __init__(self, host, port, api_version='v1'):

        if not host.startswith('http'):
            host = "http://%s" %host

        self.url = "%s:%s/%s" %(host, port, api_version)

    def __str__(self):
        return "Clair URL: %s" %self.url

    def __repr__(self):
        return self.__str__()

    def scan(self, targz_url, name):
        url = os.path.join(self.url, 'layers')

        data = {'Name': name,
                'Path': targz_url,
                'Parentname': '',
                'Format': 'Docker' }
 
        response = requests.post(url, json={'Layer': data })

        if response.status_code != 201:
            print('Error creating %s at %s' %(data['Path'], url))
            sys.exit(1)


    def report(self, name):
        '''generate a report for an image of interest. The name should
           correspond to the same name used when adding the layer...

           Parameters
           ==========
        '''

        url = os.path.join(self.url, 'layers', name)
        response = requests.get(url, params={'features': True,
                                             'vulnerabilities': True})
        if response.status_code == 200:
            return response.json()
        else:
            print('Error with %s' %url)
            sys.exit(1)


    def ping(self):
        '''ping serves as a health check. If healthy, will return True.
           We do this because the user is starting Clair as
           a separate (Docker) image and it might be the case that the
           server port/host are not correctly set.

           Returns
           =======
           healthy: If healthy, returns True, otherwise False

        '''
        url = os.path.join(self.url, 'namespaces')
        response = requests.get(url)

        try:
            if response.status_code != 200:
                return not healthy
            namespaces = response.json()['Namespaces']
            print('Found %s Clair namespaces' %len(namespaces))
            return True
        except:
            print('Cannot find Clair running at %s' %url)
        return False


    def print(self, report):
        '''print the report items'''

        if "Features" in report['Layer']:
            items = report['Layer']['Features']

            for item in items:
                if 'Vulnerabilities' in item:
                    print("%s - %s" % (item['Name'], item['Version']))
                    print("-" * len(item['Name'] + ' - ' + item['Version']))
                    for v in item['Vulnerabilities']:
                        print(v['Name'] + ' (' + v['Severity'] + ')')
                        print(v['Link'])
                        print(v['Description'])
                        print("\n")
        else:
            print("%s does not have any vulnerabilities!" %report['Layer']['Name'])
