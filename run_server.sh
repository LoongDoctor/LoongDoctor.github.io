#!/usr/bin/env sh

export LANG="en_US.UTF-8"
export LC_ALL="en_US.UTF-8"

bundle exec jekyll serve --host 127.0.0.1 --port "${PORT:-4000}"
