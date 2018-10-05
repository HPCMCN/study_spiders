#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Power by HPCM   2018-09-30 18:39:09


class SpiderMiddleware(object):
    def process_request(self, request):
        print("[INFO] spider_mid process_request: {}".format(request.url))
        return request

    def process_item(self, item):
        print("[INFO] spider_mid process_item: {}".format(item.data["url"]))
        return item


class DownloadMiddleware(object):
    def process_request(self, request):
        print("[INFO] download_mid process_item: {}".format(request.url))
        return request

    def process_item(self, item):
        print("[INFO] download_mid process_item: {}".format(item.data["url"]))
        return item

    def process_response(self, response):
        return response