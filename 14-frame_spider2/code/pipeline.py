#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Power by HPCM   2018-09-30 18:30:08
from spider import BaiduSpider

class BaiduPipeline(object):
    def process_item(self, item, spider):
        if isinstance(spider, BaiduSpider):
            print(u"[INFO] pipeline process_item: {}".format(item.data["title"]))
        return item

class BaiduPipline2(object):
    def process_item(self, item, spider):
        if isinstance(spider, BaiduSpider):
            print(u"[INFO] pipeline2 process_item: {}".format(item.data["title"]))
