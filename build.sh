#!/bin/bash

set -e 
echo "Generating additional filters..."
./gen_category_filters.py
echo "Building docker image ..."
docker build . -t elk-save-money
echo "Build successful."

