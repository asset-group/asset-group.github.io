#!/usr/bin/env bash

sudo /etc/init.d/docker start || true # Fix for WSL2

echo "Starting Jekyll container to serve content..."
sudo docker run -it --rm -p \
3030:3030 --volume="$(pwd):/srv/jekyll" \
--rm megarbelini/asset-jekyll:4.0.0 jekyll serve --port 3030
