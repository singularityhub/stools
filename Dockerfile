FROM singularityware/singularity:v3.2.1-slim as base

################################################################################
#
# Copyright (C) 2019 Vanessa Sochat.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public
# License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
################################################################################

# docker build -t vanessa/stools-clair .

# See https://docs.docker.com/develop/develop-images/multistage-build/
# for more information on multi-stage builds.
FROM arminc/clair-local-scan:v2.0.8_0ed98e9ead65a51ba53f7cc53fa5e80c92169207 as clair
COPY --from=base /usr/local/singularity /usr/local/singularity

RUN apk add --no-cache ca-certificates libseccomp squashfs-tools git
RUN apk add --update alpine-sdk

RUN mkdir -p /code /opt /var/www/images
ADD . /code/
WORKDIR /code
RUN apk add wget python3 python3-dev nginx vim xz
RUN wget https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py
RUN python3 setup.py install
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install -r /code/requirements.txt

ENV PATH="/usr/local/singularity/bin:$PATH"
