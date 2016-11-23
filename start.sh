#!/bin/bash

set -e

if `echo $@|grep -q '\-\-develop'` ; then 
    # reflect local conf changes in the container instantly
    DEVELOP="-v $PWD/logstash.conf.d:/etc/logstash/conf.d"
    echo "Starting in develop mode"
fi
echo "Creating container"
docker create -p 5601:5601 -p 6006:6006 -v elk-save-money:/var/lib/elasticsearch $DEVELOP  --name elk-save-money elk-save-money
if [ -f finances.tar.gz ] ; then 
    echo "Restoring existing data"
    docker run --rm --volumes-from elk-save-money -v $(pwd):/backup elk-save-money tar xzf /backup/finances.tar.gz
fi
echo "Starting container"
docker start elk-save-money
echo "Everything started successfully"
