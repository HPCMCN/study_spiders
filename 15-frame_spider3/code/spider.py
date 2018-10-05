#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Power by HPCM   2018-09-28 15:35:26
from myscrapy.core.spider import Spider


class BaiduSpider(Spider):
    """指定url"""
    start_urls = (
        "http://www.baidu.com/",
        "http://news.baidu.com/",
        "http://www.baidu.com/",
    )
