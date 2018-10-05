#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Power by HPCM   2018-10-05 19:25:22

from myscrapy.core.spider import Spider
from myscrapy.http.item import Item
from myscrapy.http.request import Request


class DoubanSpider(Spider):
    name = "douban"
    start_urls = ["https://movie.douban.com/top250?start=" + str(page) for page in range(0, 226, 25)]

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        "Connection": "keep-alive",
        "Host": "movie.douban.com",
        "Referer": "https://movie.douban.com/top250?start=0",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
    }

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, headers=self.headers)

    def parse(self, response):
        node_list = response.xpath("//div[@class='hd']/a")
        for node in node_list:
            data = {
                "url": node.xpath("./@href")[0],
                "title": node.xpath("./span[1]/text()")[0]
            }
            yield Item(data)
