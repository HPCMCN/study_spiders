# /usr/bin/env python
# -*- coding:utf-8 -*-
# Power by HPCM   2018-09-27 14:52:27
from abc import abstractmethod

from ..http.request import Request


class Spider(object):
    """爬虫父类"""
    tag = "spider"
    start_url = (
        "http://www.baidu.com/",
        "http://news.baidu.com/",
        "http://www.baidu.com")

    def start_requests(self):
        for start_url in self.start_url:
            yield Request(start_url)

    @abstractmethod  # 强制继承必须重写此方法
    def parse(self, response):
        """解析相应"""
        pass
