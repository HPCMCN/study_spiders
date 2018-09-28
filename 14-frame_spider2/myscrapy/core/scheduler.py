#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Power by HPCM   2018-09-27 15:09:53


from six.moves.queue import Queue



class Scheduler(object):
    """调度url请求"""
    def __init__(self):
        # 请求队列
        self.request_queue = Queue()
        # 请求指纹
        self.fingerprint = set()

    def add_request(self, request):
        """判断并添加url到指纹集合中"""
        if self._filter_request(request):
            self.request_queue.put(request)
            self.fingerprint.add(request.url)

    def _filter_request(self, request):
        """判断url是否存在于指纹集合中"""
        return request.url not in self.fingerprint

    def get_request(self):
        """获取url"""
        try:
            return self.request_queue.get(False)
        except Exception:
            return None
