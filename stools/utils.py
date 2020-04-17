'''

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

'''

import tempfile
import os


def get_temporary_name(tmpdir=None, prefix='stools', ext=''):
    '''generate a named temporary file in some temporary directory.
       This generates the name and not the actual file, it is up to the
       calling function to generate the structure.

       Parameters
       ==========
       tmpdir: the temporary directory to create the file
       prefix: the prefix of the file.
       ext: the extension of the file (default .tar.gz)

    '''
    if ext not in [None, '']:
        if not ext.startswith('.'):
            ext = '.%s' %ext

    if tmpdir == None:
        tmpdir = tempfile.mkdtemp()

    name = "%s.%s%s" %(prefix, next(tempfile._get_candidate_names()), ext)
    return os.path.join(tmpdir, name)
