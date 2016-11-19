# elk-save-money
Use an ELK stack to analyse finances and save some money

Usage
=====

Minor adjustments will likely be needed to the sample_preapre_input.sh script to match your
statements. 

    # first time only 
    docker build . -t elk-save-money 
    docker run -p 5601:5601 -p 6006:6006 --name elk-save-money -v elk-save-money:/var/lib/elasticsearch elk-save-money
    
    # or just start it if not the first time 
    docker start elk-save-money

    # push statement into the stack
    ./sample_prepare_input.sh <<Path to XLS>>

    # logstash conf changes can be deployed with
    docker cp 20-logstash.conf elk-save-money:/etc/logstash/conf.d/ 

How it works ?
==============

Brings up an [ELK stack in docker](https://elk-docker.readthedocs.io/).

Logstash is configured with a 
[tcp input](https://www.elastic.co/guide/en/logstash/current/plugins-inputs-tcp.html)
and a [csv filter](https://www.elastic.co/guide/en/logstash/current/plugins-filters-csv.html) 
to be able to ingest credit card statements in CSV format. 

A series of other filters are applied to process the data:
- [date](https://www.elastic.co/guide/en/logstash/current/plugins-filters-date.html) to set the
    correct date.
- [grok](https://www.elastic.co/guide/en/logstash/current/plugins-filters-grok.html) to get a category.

The processed credit card statement finds it's way into elastic search.
Kibana generates nice visuals and let's you search explore your statement. 

The nice visuals help you understand spending and spend less.

Security ?
==========

The security data is stored in a [docker volume](https://docs.docker.com/engine/tutorials/dockervolumes/).
You can see where this is actually stored on disk with :
    
    docker inspect elk-save-money | jq '.[0].Mounts'


