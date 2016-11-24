#!/bin/bash

set -e

if [ -z "$1" ] ; then 
    echo "Usage: $0 <<directory>>"
    exit 1
fi

find $1 -name '*.xls' | parallel -n 4 --eta --bar ./sample_prepare_input.sh {}
