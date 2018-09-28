# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from datetime import datetime
import json
from .items import TencentItem, PositionItem

class TencentPipeline(object):
    def open_spider(self, spider):
        self.f = open("tencent.json", "w")

    def process_item(self, item, spider):
        if isinstance(item, TencentItem):
            item["time"] = str(datetime.now())
            item["source"] = str(spider.name)
            json_str = json.dumps(dict(item)) + ", \r\n"
            self.f.write(json_str)
        return item

    def close_spider(self, spider):
        self.f.close()


class PositionJsonPipeline(object):
    def open_spider(self, spider):
        self.f = open("position.json", "w")

    def process_item(self, item, spider):
        if isinstance(item, PositionItem):
            json_str = json.dumps(dict(item)) + ", \r\n"
            self.f.write(json_str)
        return item

    def close_spider(self, spider):
        self.f.close()
 
