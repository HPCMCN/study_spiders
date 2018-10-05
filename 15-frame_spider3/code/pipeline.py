#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Power by HPCM   2018-09-30 18:30:08
from baidu import BaiduSpider
from Douban import DoubanSpider

class BaiduPipeline(object):
    def process_item(self, item, spider):
        if isinstance(spider, BaiduSpider):
            print(u"[INFO] pipeline process_item: {}".format(item.data["title"]))
        return item

class DoubanPipeline(object):
    def process_item(self, item, spider):
        if isinstance(spider, DoubanSpider):
            print(u"[INFO] pipeline process_item: {}".format(item.data["title"]))
