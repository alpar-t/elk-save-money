#!/bin/bash
docker create -p 5601:5601 -p 6006:6006 -v elk-save-money:/var/lib/elasticsearch  --name elk-save-money elk-save-money
if [ -f finances.tar.gz ] ; then 
    docker run --rm --volumes-from elk-save-money -v $(pwd):/backup elk-save-money tar xzf /backup/finances.tar.gz
fi
docker start elk-save-money
