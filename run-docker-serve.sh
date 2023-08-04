#!/usr/bin/env bash

sudo docker run -it --rm -p \
3030:3030 --volume="$(pwd):/srv/jekyll" \
--rm megarbelini/asset-jekyll:4.0.0 jekyll serve --port 3030
