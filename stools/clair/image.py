"""

Copyright (C) 2018-2022 Vanessa Sochat.

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


from spython.main import Client
from stools.utils import get_temporary_name
import hashlib
import tempfile
import tarfile
import shutil
import os


def export_to_targz(image, tmpdir=None):
    """export a Singularity image to a .tar.gz file. If run within a docker
    image, you should set via_build to false (as sudo will work under
    priviledged). Outside of Docker as regular user, via_build works
    better.

    Parameters
    ==========
    image: the full path to the Singularity image
    tmpdir: a temporary directory to export to.

    """
    print("Exporting %s to targz..." % image)

    if tmpdir == None:
        tmpdir = tempfile.mkdtemp()

    # We will build into this directory (sandbox) to export without sudo
    export_dir = get_temporary_name(tmpdir, "singularity-clair")
    targz = "%s.gz" % export_dir

    sandbox = Client.build(image, export_dir, sandbox=True, sudo=False)

    # Write the tarfile
    with tarfile.open(targz, "w:gz") as tar:
        tar.add(sandbox, arcname="/")

    shutil.rmtree(sandbox)

    if os.path.exists(targz):
        return targz


def sha256(image, block_size=65536):
    """create a dummy Docker image name (the sha256 sum)
    https://gist.github.com/rji/b38c7238128edf53a181
    """
    hashsum = hashlib.sha256()
    with open(image, "rb") as filey:
        for chunk in iter(lambda: filey.read(block_size), b""):
            hashsum.update(chunk)
    return hashsum.hexdigest()
