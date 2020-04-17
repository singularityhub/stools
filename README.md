# Singularity Container Tools

These are tools for Singularity containers, optimized for using with continuous integration for security
and quality checks. For an example of the package being used in a continuous integration context, see the [stools-clair](https://github.com/singularityhub/stools-clair) repository.

[![asciicast](https://asciinema.org/a/178712.png)](https://asciinema.org/a/178712)

In this work we will use [Clair OS](https://github.com/coreos/clair) combined with Continuous Integration
(travis and circle) to scan [Singularity](https://singularityware.github.io) containers for security
vulnerabilities. 

## Tags

 - [v2.4.5](https://github.com/singularityhub/stools/tree/v2.4.5) Uses Singularity v2.4.5
 - [v3.2.1 (master)](https://github.com/singularityhub/stools) Uses Singularity v3.2.1

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

If you want, build the container (or use from Docker Hub)

```bash
$ docker build -t vanessa/stools-clair .
```

Start the application with docker compose. Note that you should have the images you want to scan in the $PWD, which will be mapped to the container in `/code` (see the docker-compose.yml file). You can change this around, just be sure that the containers you want to add are here. I'll be updating this so the server inside can accept a post for an external container, but I need some sleep first :)

```bash
$ docker-compose up -d
```

Scan a local image in $PWD mapped to /code in the container. If you didn't clone the repo, make sure you get the [docker-compose.yml](https://github.com/singularityhub/stools/blob/master/docker-compose.yml) file first!

```bash
$ singularity pull shub://vsoch/singularity-images
$ docker exec -it clair-scanner sclair singularity-images_latest.sif
```

By default, reports are printed to stdout. Saving reports is enabled by using the `--report` flag which will save the report as JSON in $PWD/reports and not print to stdout. Additionally, `--report` accepts a directory path which will tell `sclair` where to save reports.

```bash
$ docker exec -it clair-scanner sclair singularity-images_latest.sif --report
```

Change between JSON or an HTML table reports by adding the `--report-format` flag followed by `json` or `html`.

```bash
$ docker exec -it clair-scanner sclair singularity-images_latest.sif --report --report-format html
```

For a full example (using a container with a known vulnerability) see
the [example test](test) folder.
