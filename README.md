# Singularity Container Tools

These are tools for Singularity containers, optimized for using with continuous integration for security
and quality checks. Right now the package is under development, and these general notes are provided for
refernece.

In this work we will use [Clair OS](https://github.com/coreos/clair) combined with Continuous Integration
(travis and circle) to scan [Singularity](https://singularityware.github.io) containers for security
vulnerabilities. 

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

Install

```bash
pip install stools
```

Start the Clair Server (you need Docker installed)

```bash
./start-clair
```

Scan local images

```bash
sclair vsoch-hello-world.simg
```
