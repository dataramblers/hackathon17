#!/usr/bin/env python3

from elasticsearch import Elasticsearch
import json
import gzip
import pyisbn
import os
import time
import argparse
from tqdm import tqdm


class Importer:

    """
    A simple class to build a elastic search index for the crossref data
    """

    def __init__(self, es_host="localhost", es_port=9200):
        self.es = Elasticsearch(hosts=[{'host': es_host, 'port': es_port}],)

    def batch(self, index, doc_type, body, counter=0):
        """
        Load data into the index
        :param index: Name of the index
        :param doc_type: Name of the doc_type
        :param body: Data to index
        :param counter: internal counter for failure retry
        :return:
        """
        try:
            self.es.bulk(index=index, doc_type=doc_type, body=body)
        except Exception:
            print("Error: Failed to import a part of the data set. "
                  "Try again to import segment for the {} time".format(counter + 1))
            time.sleep(10)
            counter += 1
            self.batch(index, doc_type, body, counter)

    def bootstrap(self, index, doc_type, mapping_file="mapping.json"):
        """
        Bootstrap es index. Delete existing index and create a new one with mapping
        :param index: Name of the index
        :param doc_type: Name of the doc_type
        :param mapping_file: The definition for the mapping
        :return:
        """
        mapping = open(mapping_file).read()
        if self.es.indices.exists(index):
            self.es.indices.delete(index)
        self.es.indices.create(index, mapping)

    def remove_affiliation(self, json_object, parent_json_obj):
        """
        Removes `affiliation` field in embedded person object
        :param json_object: The current json object
        :param parent_json_obj: Either 'author' or 'editor'
        :return:
        """
        if parent_json_obj in json_object.keys():
            for t in json_object[parent_json_obj]:
                t.pop('affiliation', None)
        return json_object

    def load(self, directory, index="crossref", doc_type="crossref", bulk_size=50000):
        """
        Load data for a file into Es-Index
        :param directory: The path for the directory with the data
        :param index: Name of the index
        :param doc_type: Name of the doc_type
        :param bulk_size: The bulksize for committing the data into the es index
        :return:
        """
        cache = list()
        counter = 0
        total = len([name for name in os.listdir(directory) if os.path.join(directory, name) and name.endswith('json.gz')])
        with tqdm(total=total) as pbar:
            for root, dir_names, file_names in os.walk(directory):
                for filename in file_names:
                    if filename.endswith('json.gz'):
                        pbar.update()
                        with gzip.open(os.path.join(root, filename), 'rb') as f:
                            json_objects = json.loads(f.read())
                            for json_object in json_objects:
                                doc_id = json_object['DOI']
                                # convert isbn numbers
                                if 'ISBN' in json_object.keys():
                                    isbn_list = list()
                                    for isbn in json_object['ISBN']:
                                        if len(isbn.replace('-', '')) == 10:
                                            isbn_list.append(pyisbn.convert(isbn))
                                    json_object['ISBN'] = isbn_list
                                json_object = self.remove_affiliation(json_object, 'author')
                                json_object = self.remove_affiliation(json_object, 'editor')
                                header = '{ "index" : { "_index" : "' + index + '", "_type" : "' + doc_type + '", "_id" : "' + str(hash(doc_id)) + '" } }'
                                cache.append(header)
                                cache.append(json.dumps(json_object))
                                counter += 1
                                if counter >= bulk_size:
                                    self.batch(index, doc_type, "\n".join(cache))
                                    cache = []
                                    counter = 0
        pbar.close()


parser = argparse.ArgumentParser(description='Load json data fro crossref into an elastic search index.')
parser.add_argument('data', type=str, help='Path to the gziped data')
parser.add_argument('--es-host', type=str, help='Elastic search uri', default="localhost")
parser.add_argument('--es-port', type=int, help='Elastic search uri', default=9200)
parser.add_argument('--es-index',  type=str, help='Elastic search index', default="crossref")
parser.add_argument('--es-doc-type',  type=str, help='Elastic search doctype', default="crossref")
parser.add_argument('--es-flush',  type=bool, help='Flush and create the elastic search index', default=False)
parser.add_argument('--mapping-file',  type=str, help='Mapping file for the index', default="mapping.json")
parser.add_argument('--bulk-size', type=int, help='Bulk size for the import', default=50000)
args = parser.parse_args()
importer = Importer(args.es_host, args.es_port)
# flush data and create index
if args.es_flush:
    importer.bootstrap(args.es_index, args.es_doc_type, args.mapping_file)
# import data
importer.load(args.data, args.es_index, args.es_doc_type, args.bulk_size)
