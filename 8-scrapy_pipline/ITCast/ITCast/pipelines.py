# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

import pymongo


class ItcastPipeline(object):
    def open_spider(self, spider):
        self.f = open("itcast.json", "w")

    def process_item(self, item, spider):
        json_str = json.dumps(dict(item))
        self.f.write(json_str)
        return item

    def close_spider(self, spider):
        self.f.close()


class ItcastMongoPipeline(object):
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(host="localhost", port=27017)
        self.collection = self.client.itcast.teacher

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
