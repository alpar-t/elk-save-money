# elk-save-money
Use an ELK stack to analyse finances and save some money


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
- [grok](https://www.elastic.co/guide/en/logstash/current/plugins-filters-grok.html) and 
- [mutate](https://www.elastic.co/guide/en/logstash/current/plugins-filters-mutate.html) at least to
    get a category.

The processed credit card statement finds it's way into elastic search.
Kibana generates nice visuals and let's you search explore your statement. 

The nice visuals help you understand spending and spend less.


