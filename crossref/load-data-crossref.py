#!/usr/bin/env python3

from elasticsearch import Elasticsearch
from sys import argv
import json
import gzip
import pyisbn
import os

def removeAffiliation(parentJsonObj):
    '''
    Removes `affiliation` field in embedded person object
    :param parentJsonObj: Either 'author' or 'editor'
    :return:
    '''
    if parentJsonObj in jsonobj.keys():
        for t in jsonobj[parentJsonObj]:
            t.pop('affiliation', None)

index = 'crossref'
doctype = 'crossref'
es = Elasticsearch()
cache = list()
counter = 0
bulksize = 30000

for dirname, dirnames, filenames in os.walk(argv[1]):
    for filename in filenames:
        if filename.endswith('json.gz'):
            with gzip.open(os.path.join(dirname,filename), 'rb') as f:
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
                        removeAffiliation('author')
                        removeAffiliation('editor')
                        header = '{ "index" : { "_index" : "' + index + '", "_type" : "' + doctype + '", "_id" : "' + str(hash(id)) + '" } }'
                        cache.append(header)
                        cache.append(json.dumps(jsonobj))
                        counter = counter + 1
                        if counter >= bulksize:
                            es.bulk(index=index, doc_type=doctype, body='\n'.join(cache))
                            cache = []
                            counter = 0
