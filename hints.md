# Some hints

## Docker compose
* https://docs.docker.com/compose/overview
* https://docs.docker.com/compose/gettingstarted/
* https://docs.docker.com/compose/networking/

## Docker containers
* https://www.elastic.co/guide/en/elasticsearch/reference/current/docker.html

## Use cases 
* https://qbox.io/blog/kafka-and-elasticsearch-a-perfect-match-1
* https://github.com/hannesstockner/kafka-connect-elasticsearch
* https://data-artisans.com/blog/kafka-flink-a-practical-how-to

## jwilder/nginx-proxy
If you use jwilder/nginx-proxy as a reversed proxy, you need to attach the network hackathon to the proxy container
```bash
docker network connect hackathon17_hackathon $(docker ps | grep jwilder/nginx-proxy | cut -f 1 -d ' ')

```