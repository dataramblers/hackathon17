from elasticsearch import Elasticsearch
from sys import argv
import json
import gzip

index = 'edoc'
doctype = 'edoc'
# es = Elasticsearch(http_auth=('elastic', 'changeme'))
es = Elasticsearch()

with gzip.open(argv[1], 'rb') as f:
    for l in f:
        id = json.loads(l)['eprintid']
        es.create(index=index, doc_type=doctype, id=id, body=l)
