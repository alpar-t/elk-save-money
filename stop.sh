#!/bin/bash
set -e
echo "Stopping and extracting data..."
docker stop elk-save-money
docker run --rm --volumes-from elk-save-money -v $(pwd):/backup elk-save-money tar cfz /backup/finances.tar.gz /var/lib/elasticsearch
echo "Cleaning up ..."
docker rm -f elk-save-money
docker volume rm elk-save-money
echo "Everything stopped"
