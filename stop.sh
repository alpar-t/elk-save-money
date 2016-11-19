#!/bin/bash
set -e
docker stop elk-save-money
docker run --rm --volumes-from elk-save-money -v $(pwd):/backup elk-save-money tar cfz /backup/finances.tar.gz /var/lib/elasticsearch
docker rm -f elk-save-money
docker volume rm elk-save-money

