#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Power by HPCM   2018-09-27 14:58:05


# noinspection SpellCheckingInspection
class Request(object):
    """请求url"""

    def __init__(self, url, method=None, headers=None, params=None, formdata=None,
                 proxy=None, callback=None, dont_filter=None, meta=None):
        self.url = url
        self.method = method or "GET"
        self.headers = headers or {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (\
            KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
        self.params = params
        self.formdata = formdata
        self.proxy = proxy
        self.callback = callback or "parse"
        self.dont_filter = dont_filter
        self.meta = meta
