#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Power by HPCM   2018-09-28 15:42:27


class SpiderMiddleware(object):
    def process_request(self, request):
        print("[INFO] spiderMiddleware-process_request: {}".format(request.url))
        return request

    def process_item(self, item):
        print("[INFO] spiderMiddleware-process_item: {}".format(item.data["url"]))
        return item
