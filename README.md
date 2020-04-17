# Singularity Container Tools

These are tools for Singularity containers, optimized for using with continuous integration for security
and quality checks. For an example of the package being used in a continuous integration context, see the [stools-clair](https://github.com/singularityhub/stools-clair) repository.

[![asciicast](https://asciinema.org/a/178712.png)](https://asciinema.org/a/178712)

In this work we will use [Clair OS](https://github.com/coreos/clair) combined with Continuous Integration
(travis and circle) to scan [Singularity](https://singularityware.github.io) containers for security
vulnerabilities. 

## Tags

 - [v3.2.1 (master)](https://github.com/singularityhub/stools) Uses Singularity v3.2.1 and above
 - [v2.4.5](https://github.com/singularityhub/stools/tree/v2.4.5) Uses Singularity v2.4.5

## Background
Clair is intended to run as a server to continuous scan Docker *layers* for vulnerabilities. This doesn't map
well to the research domain because of the following:

 - Docker containers come in layers (.tar.gz files) while Singularity images are single binary files that don't "plug in" nicely to Clair.
 - Most researchers can't support continuous running of such a service.

On the other hand, a typical researcher *does* use services like [TravisCI](https://travis-ci.org) and [CircleCI](https://circle-ci.org) to
run their code bases against tests. Since these services now offer running containers and other service-type things, we in fact could do the following:

 - Spin up a Clair server during testing
 - Build a Singularity image, and scan the filesystem contents (before finalized in the image).

While this isn't a continually running service, we can minimally ensure that a container is scanned each time
it is built (and then likely merged to be used in production). If the user takes advantage of [Singularity Hub](https://www.singularity-hub.org) or [Singularity Registry Server](https://singularityhub.github.io/sregistry) the image will be pushed or built for production after passing 
these various tests.

This experiment is based on early discussion in [this thread](https://github.com/singularityhub/sregistry/issues/14).


## Basic Usage

You'll need to first clone the repository:

```bash
git clone https://github.com/singularityhub/stools
cd stools
```

### Build Containers

If you want, build the container (or use a tagged release from [Docker Hub](https://hub.docker.com/repository/registry-1.docker.io/vanessa/stools-clair/tags?page=1)).

```bash
$ docker build -t vanessa/stools-clair .
```

Start the application with [docker compose](https://docs.docker.com/compose/install/). 
Note that you should have the images you want to scan in the $PWD, which will be mapped to the container in `/code` 
(see the [docker-compose.yml](docker-compose.yml) file). You can change this around, just be sure that the containers you want to add are here.

```bash
$ docker-compose up -d
```

Make sure that your containers are up and running! There is one for the clair server
that we will interact with, and one for the database.

```bash
$ docker-compose ps
    Name                   Command               State                            Ports                          
-----------------------------------------------------------------------------------------------------------------
clair-db        docker-entrypoint.sh postgres    Up      0.0.0.0:5432->5432/tcp                                  
clair-scanner   /clair -config=/config/con ...   Up      0.0.0.0:6060->6060/tcp, 6061/tcp, 0.0.0.0:8080->8080/tcp
```

Also note that the folder [reports](reports) by way of being in the mounted present working
directory, will appear at `/code/reports` in the container. We will need to know this later.

### Scan an Image

Let's scan a local image in $PWD mapped to /code in the container. First
pull one from your registry of choice:

```bash
$ singularity pull shub://vsoch/singularity-images
```

And now let's scan! We do this by executing a command to the `clair-scanner` container.
The most basic usage will just print a report to stdout, like this:

```bash
$ docker exec -it clair-scanner sclair singularity-images_latest.sif
...

CVE-2016-9843 (Low)
http://people.ubuntu.com/~ubuntu-security/cve/CVE-2016-9843
The crc32_big function in crc32.c in zlib 1.2.8 might allow context-dependent attackers to have unspecified impact via vectors involving big-endian CRC calculation.
```

### Save a Report

However, if you want to save a report to file (json), you can add the `--report` argument
pointing to an existing output directory of choice. For example, since [reports](reports)
is provided in our present working directory and already bound to the container at `/code/reports`
we can specify that as an argument:

```bash
$ docker exec -it clair-scanner sclair --report /code/reports singularity-images_latest.sif
```

Using `--report` will not disable the print to stdout. However, if you want to disable it,
you can add the `--no-print` option. An example JSON report can be found in the [reports](reports) folder.

```bash
$ docker exec -it clair-scanner sclair --report /code/reports --no-print singularity-images_latest.sif
```

For a full example of what is printed to stdout (using a container with a known vulnerability) see
the [example test](test) folder.
