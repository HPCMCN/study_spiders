#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Power by HPCM   2018-09-27 15:03:34

class Response(object):
    """响应类"""
    def __init__(self, url, content, headers, encoding, status_code):
        self.url = url, 
        self.content = content, 
        self.headers = headers
        self.encoding = encoding
        self.status_code = status_code
