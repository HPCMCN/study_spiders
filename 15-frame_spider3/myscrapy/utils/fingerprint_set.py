# coding=utf-8
import redis

from ..config.default_setting import *


class PythonFingerprintSet(object):
    """python set保存指纹接口兼容"""
    def __init__(self):
        self.fp_set = set()

    def add(self, fp):
        self.fp_set.add(fp)

    def filter_fp(self, fp):
        return fp in self.fp_set


class RedisFingerprintSet(object):
    """"redis保存指纹接口兼容"""
    def __init__(self):
        self.redis_client = redis.Redis(host=REDIS_SET_HOST, port=REDIS_SET_PORT, db=REDIS_SET_DB)

    def add(self, fp):
        self.redis_client.sadd(REDIS_SET_NAME, fp)

    def filter_fp(self, fp):
        return self.redis_client.sismember(REDIS_SET_NAME, fp)
