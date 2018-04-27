FROM arminc/clair-local-scan:v2.0.0

# docker build -t vanessa/stools-clair .

RUN apk update && apk add \
    cmake \
    openssl \
    python3 \
    nginx \
    wget \
    git \
    vim

RUN apk add --update alpine-sdk
RUN apk add g++ libtool musl-dev linux-headers squashfs-tools

RUN mkdir -p /code /opt /var/www/images
ADD . /code

WORKDIR /opt
RUN wget https://github.com/singularityware/singularity/releases/download/2.4.5/singularity-2.4.5.tar.gz && \
    tar xvf singularity-2.4.5.tar.gz && cd singularity-2.4.5 && ./configure --prefix=/usr/local && make && make install

ADD . /code/
WORKDIR /code
RUN wget https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py
RUN python3 setup.py install
RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install -r /code/requirements.txt
