FROM sebp/elk:latest
ADD logstash.conf.d  /etc/logstash/conf.d 
EXPOSE 6006
EXPOSE 5601
ENV LS_OPTS="--config.reload.automatic"
RUN /opt/logstash/bin/logstash-plugin install logstash-filter-checksum && \
    /opt/logstash/bin/logstash-plugin install logstash-filter-elasticsearch
