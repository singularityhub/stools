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
import hashlib
import tempfile
import shutil
import os


def export_to_targz(image, tmpdir=None, via_build=True):
    '''export a Singularity image to a .tar.gz file. If run within a docker
       image, you should set via_build to false (as sudo will work under
       priviledged). Outside of Docker as regular user, via_build works
       better.

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
    tar = "%s.tar" %export_dir
    targz = "%s.gz" %tar

    if via_build is True:

        sandbox = Client.build(image, export_dir, sandbox=True, sudo=False)
    
        # Create the .tar, then .tar.gz 

        cmd = ["tar", "-cf", tar, sandbox]
        Client._run_command(cmd)
        shutil.rmtree(sandbox)


    else:

        # Requires sudo
        Client.image.export(image, tar)

    cmd = ["gzip", tar]
    Client._run_command(cmd)

    if os.path.exists(targz):
        return targz


def sha256(image, block_size=65536):
    '''create a dummy Docker image name (the sha256 sum)
       https://gist.github.com/rji/b38c7238128edf53a181
    '''
    hashsum = hashlib.sha256()
    with open(image, "rb") as filey:
        for chunk in iter(lambda: filey.read(block_size), b""):
            hashsum.update(chunk)
    return hashsum.hexdigest()
