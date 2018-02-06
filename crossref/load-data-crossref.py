#!/usr/bin/env python3

from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import json
import lzma
import pyisbn
import os
import argparse
import time
from tqdm import tqdm


class Importer:

    """
    A simple class to build a elastic search index for the crossref data
    """

    def __init__(self, es_host="localhost", es_port=8080):
        self.es = Elasticsearch([es_host + ':' + str(es_port) + '/'], timeout=3000)
        self.deleted_key = list()

    def batch(self, body):
        """
        Load data into the index
        :param body: Data to index
        :return:
        """
        errors = bulk(self.es, actions=body, raise_on_error=False)
        if errors[0] < 10000:
            with open('./logging/logs-' + str(time.time()) + '.json', 'w') as file:
                file.write(json.dumps(errors[1], ensure_ascii=False, indent='    '))

        print(errors)

    def bootstrap(self, index, mapping_file="mapping.json"):
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
        self.es.indices.create(index)
        self.es.indices.put_template('crossref', mapping)

    @staticmethod
    def remove_affiliation(json_object, parent_json_obj):
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

    def remove_unused_fields(self, json_object: dict):
        used_fields = ['ISBN', 'ISSN', 'title', 'author', 'editor', 'subtitle', 'DOI', 'funder', 'published-print']
        removal_keys = list()
        for key in json_object:
            if not used_fields.__contains__(key):
                removal_keys.append(key)

        for key in removal_keys:
            if not self.deleted_key.__contains__(key):
                self.deleted_key.append(key)
            del json_object[key]
        return json_object

    def load(self, directory, index="crossref", doc_type="crossref", bulk_size=100000):
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
        # total = len([name for name in os.listdir(directory) if os.path.join(directory, name) and name.endswith('json.xz')])
        # with tqdm(total=total) as pbar_o:
        for root, dir_names, file_names in os.walk(directory):
            for filename in file_names:
                if filename.endswith('json.xz'):
                    print("OPEN FILE")
                    # pbar_o.update()
                    with lzma.open(os.path.join(root, filename), 'rt', encoding='utf-8') as f:
                        line = f.readline()
                        while line:
                            json_object = json.loads(line)
                            # json_object['oid'] = json_object['_id']['$oid']
                            # del json_object['_id']
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
                            json_object = self.remove_unused_fields(json_object)
                            data = dict()
                            data['_op_type'] = 'index'
                            data['_index'] = index
                            data['_type'] = doc_type
                            data['_id'] = doc_id
                            data['_source'] = json_object
                            cache.append(data)
                            counter += 1
                            if counter >= bulk_size:
                                self.batch(cache)
                                cache = []
                                counter = 0
                            line = f.readline()
                    # after each file write down what keys were deleted.
                    with open('logging/deleted_keys.txt', 'w', encoding='utf-8') as file:
                        for key in self.deleted_key:
                            file.write(key + '\n')
        # pbar_o.close()


parser = argparse.ArgumentParser(description='Load json data fro crossref into an elastic search index.')
parser.add_argument('data', type=str, help='Path to the gziped data')
parser.add_argument('--es-host', type=str, help='Elastic search uri', default="sb-ues2.swissbib.unibas.ch")
parser.add_argument('--es-port', type=int, help='Elastic search uri', default=8080)
parser.add_argument('--es-index',  type=str, help='Elastic search index', default="crossref")
parser.add_argument('--es-doc-type',  type=str, help='Elastic search doctype', default="crossref")
parser.add_argument('--es-flush',  type=bool, help='Flush and create the elastic search index', default=True)
parser.add_argument('--mapping-file',  type=str, help='Mapping file for the index', default="mapping.json")
parser.add_argument('--bulk-size', type=int, help='Bulk size for the import', default=10000)
args = parser.parse_args()
importer = Importer(args.es_host, args.es_port)
# flush data and create index
if args.es_flush:
    importer.bootstrap(args.es_index, args.mapping_file)
# import data
print(importer.es.cat.health())
importer.load(args.data, args.es_index, args.es_doc_type, args.bulk_size)
