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


from spython.main import Client
from stools.utils import get_temporary_name
import tempfile
import shutil
import os


def export_to_targz(image, tmpdir=None):
    '''export a Singularity image to a .tar.gz file. 

       Parameters
       ==========
       image: the full path to the Singularity image
       tmpdir: a temporary directory to export to.

    '''
    print("Exporting %s to targz..." %image)

    if tmpdir == None:
        tmpdir = tempfile.mkdtemp()

    # We will build into this directory (sandbox) to export without sudo

    export_dir = get_temporary_name(tmpdir, 'singularity-clair')
    sandbox = Client.build(image, export_dir, sandbox=True, sudo=False)

    # Create the .tar.gz 

    targz = "%s.tar.gz" %sandbox
    cmd = ["tar", "-zcf", targz, sandbox]
    Client.run_command(cmd)

    # Clean up the directory

    shutil.rmtree(sandbox)

    if os.path.exists(targz):
        return targz
