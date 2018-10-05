#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Power by HPCM   2018-09-28 15:46:20


class DownloadMiddleware(object):
    def process_request(self, request):
        print(u"[INFO] DownloadMiddleware-process_request: {}".format(request.url))
        return request

    def process_response(self, response):
        print(u"[INFO] DownloadMiddleware-process_response: {}".format(response.url))
        return response
