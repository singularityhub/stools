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

__version__ = "0.0.0"
AUTHOR = 'Vanessa Sochat'
AUTHOR_EMAIL = 'vsochat@stanford.edu'
NAME = 'stools'
PACKAGE_URL = "http://www.github.com/singularityhub/stools"
KEYWORDS = 'singularity container tools'
DESCRIPTION = "Command line tools for container quality assurance"
LICENSE = "LICENSE"

INSTALL_REQUIRES = (
    ('requests', {'min_version': None}),
    ('spython', {'min_version': "0.0.25"}),
)