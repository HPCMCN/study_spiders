#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Power by HPCM   2018-09-30 13:41:41

from myscrapy.core.spider import Spider

from myscrapy.http.item import Item
from myscrapy.http.request import Request


class BaiduSpider(Spider):
    name = "baidu"
    # start_urls = [
    #     "http://www.baidu.com/",
    #     "http://news.baidu.com/",
    #     "http://www.baidu.com/"
    # ]
    start_url = ["http://tieba.baidu.com/f?kw=%E7%BE%8E%E9%A3%9F&pn={}".format(page) for page in range(1, 45*3+1, 45)]

    def start_requests(self):
        for url in self.start_url:
            yield Request(url, dont_filter=True)

    def parse(self, response):
        data = {
            "title": response.xpath("//title/text()"),
            "url": response.url
        }
        yield Item(data)
