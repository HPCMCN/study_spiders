#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Power by HPCM   2018-09-27 15:09:53

from hashlib import sha1
# noinspection PyPackageRequirements
import w3lib.url
from ..config.default_setting import *
if ROLE == "master" or "slave":
    from ..utils.queue import Queue
    from ..utils.fingerprint_set import RedisFingerprintSet as Set
elif ROLE is None:
    from six.moves.queue import Queue
    from ..utils.fingerprint_set import PythonFingerprintSet as Set
else:
    raise ImportError("Not Support type of {}".format(ROLE))
# noinspection PyPackageRequirements


# noinspection PyBroadException,SpellCheckingInspection
class Scheduler(object):
    """调度url请求"""

    def __init__(self):
        # 请求队列
        self.request_queue = Queue()
        # 请求指纹
        self.fingerprint = Set()
        # 请求计数
        self.request_count = 0

    def add_request(self, request):
        """判断并添加url到指纹集合中"""
        fingerprint = self._get_fingerprint(request)
        if self._filter_request(fingerprint):
            self.request_queue.put(request)
            self.fingerprint.add(fingerprint)
            self.request_count += 1
        else:
            print("[INFO] error url: {}".format(request.url))

    def _filter_request(self, fingerprint):
        """判断url是否存在于指纹集合中"""
        return not self.fingerprint.filter_fp(fingerprint)

    @staticmethod
    def _get_fingerprint(request):
        # url规整
        url = w3lib.url.canonicalize_url(request.url).encode()
        # 请求方式规整
        method = request.method.upper().encode()
        # url传递参数规整
        params = {} if request.params is None else request.params
        params = str(sorted(params.items(), key=lambda x: x[0], reverse=True)).encode()
        # form表单参数规整
        formdata = {} if request.formdata is None else request.formdata
        formdata = str(sorted(formdata.items(), key=lambda x: x[0], reverse=True)).encode()

        s = sha1()
        s.update(url)
        s.update(method)
        s.update(params)
        s.update(formdata)
        return s.hexdigest()

    def get_request(self):
        """获取url"""
        try:
            # 非阻塞进行url获取
            return self.request_queue.get(False)
        except Exception:
            return None
