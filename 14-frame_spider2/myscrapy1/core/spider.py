#/usr/bin/env python
#-*- coding:utf-8 -*-
# Power by HPCM   2018-09-27 14:52:27


from ..http.request import Request
from ..http.item import Item

class Spider(object):
    """爬虫父类"""
    start_url = (
            "http://www.baidu.com/",
            "http://news.baidu.com/",
            "http://www.baidu.com/",)

    def start_requests(self):
        for start_url in self.start_url:
            yield Request(start_url)

    def parse(self, response):
        """解析相应"""
        data = {
                "url": response.url,
                "text": response.content
            }
        print("spider", data["url"])
        item = Item(data)

        return data
