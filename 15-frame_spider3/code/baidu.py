#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Power by HPCM   2018-09-30 13:41:41

from myscrapy.core.spider import Spider

from myscrapy.http.item import Item


class BaiduSpider(Spider):
    name = "baidu"
    start_urls = [
        "http://www.baidu.com/",
        "http://news.baidu.com/",
        "http://www.baidu.com/"
    ]

    def parse(self, response):
        data = {
            "title": response.xpath("//title/text()"),
            "url": response.url
        }
        yield Item(data)
