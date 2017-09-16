from elasticsearch import Elasticsearch
from sys import argv
import json
import gzip
import pyisbn


# def isbn10toisbn13(isbn10):
#     isbn13 = '978' + isbn10.replace('-', '')[0:9]
#     s = sum([(int(isbn13[i]) - 48) * 1 if i % 2 == 0 else 3 for i in range(0, len(isbn13))])
#     return isbn13 + str(10 - (s % 10))

# es = Elasticsearch(http_auth=('elastic', 'changeme'))
index = 'crossref'
doctype = 'crossref'
es = Elasticsearch()
cache = list()
counter = 0
bulksize = 10000

with gzip.open(argv[1], 'rb') as f:
    for l in f:
        bigjsonobject = json.loads(l)
        for jsonobj in bigjsonobject:
            id = jsonobj['DOI']
            if 'ISBN' in jsonobj.keys():
                isbnlist = list()
                for isbn in jsonobj['ISBN']:
                    if len(isbn.replace('-','')) == 10:
                        isbnlist.append(pyisbn.convert(isbn))
                jsonobj['ISBN'] = isbnlist
            header = '{ "index" : { "_index" : "' + index + '", "_type" : "' + doctype + '", "_id" : "' + str(hash(id)) + '" } }'
            cache.append(header)
            cache.append(json.dumps(jsonobj))
            counter = counter + 1
            if counter >= bulksize:
                es.bulk(index=index, doc_type=doctype, body='\n'.join(cache))
                cache = []
                counter = 0
