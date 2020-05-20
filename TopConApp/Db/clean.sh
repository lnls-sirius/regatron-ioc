#!/bin/bash
set -x
set -e
find . -name '*.pyc' -exec rm --force {} +
find . -name '*.pyo' -exec rm --force {} +
find . -name '*~'    -exec rm --force {} +
find . -name '__pycache__'  -exec rm -rd --force {} +
