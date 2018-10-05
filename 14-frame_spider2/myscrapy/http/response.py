#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Power by HPCM   2018-09-27 15:03:34
import re
import json
from lxml import etree


class Response(object):
    """响应类"""
    def __init__(self, url, content, headers, encoding, status_code, text):
        self.url = url, 
        self.content = content, 
        self.headers = headers
        self.encoding = encoding
        self.status_code = status_code
        self.text = text

    def xpath(self, rule):
        """使用xpath"""
        print(len(self.content))

        html_obj = etree.HTML(self.content[0])
        return html_obj.xpath(rule)

    def findall(self, rule):
        """正则获取所有"""
        return re.findall(rule, self.text)

    @property
    def json(self):
        """转化为Json格式"""
        return json.loads(self.content)
