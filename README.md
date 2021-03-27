# sentinel-scripts

[![Build Status](https://travis-ci.com/paulaolmedo/sentinel-scripts.svg?token=bqY7JHfPDqjwZn2ypbwq&branch=master)](https://travis-ci.com/paulaolmedo/sentinel-scripts)

Tiny script to manage (unzip and rename) Sentinel-2 MSI files

## usage
### without docke

    python src/main.py --path "path-to-your-sentinel-files"

### with docker
#### 1) build docker image
    docker build -f .ci/Dockerfile -t sentinel-scripts .
#### 2) execute it
    docker run -it -v /path-to-your-sentinel-files:/project sentinel-scripts --path /project bash
