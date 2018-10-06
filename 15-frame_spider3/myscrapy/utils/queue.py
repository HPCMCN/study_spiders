# coding=utf-8
import time
import pickle

import redis
# noinspection PyPep8Naming
from six.moves import queue as BaseQueue

from ..config.default_setting import *


class Queue(object):
    """redis与python内置Queue的借口兼容"""
    Empty = BaseQueue.Empty
    Full = BaseQueue.Full
    max_timeout = 0.3

    def __init__(self, maxsize=0, name=REDIS_QUEUE_NAME, host=REDIS_QUEUE_HOST,
                 port=REDIS_QUEUE_PORT, db=REDIS_QUEUE_DB, lazy_limit=True,
                 password=None):
        self.name = name
        self.redis = redis.StrictRedis(host=host, port=port, db=db, password=password)
        self.maxsize = maxsize
        self.lazy_limit = lazy_limit
        self.last_qsize = 0

    def qsize(self):
        """获取当前存储个数"""
        self.last_qsize = self.redis.llen(self.name)
        return self.last_qsize

    def empty(self):
        """非空判断"""
        return self.qsize() == 0

    def full(self):
        """是否存满"""
        return True if self.maxsize and self.qsize() >= self.maxsize else False

    def put_nowait(self, obj):
        """非等待存入"""
        if self.lazy_limit and self.last_qsize < self.maxsize:
            pass
        elif self.full():
            raise self.Full
        self.last_qsize = self.redis.rpush(self.name, pickle.dumps(obj))
        return True

    def put(self, obj, block=True, timeout=None):
        """等待存入redis"""
        if block is not True:
            return self.put_nowait(obj)

        start_time = time.time()
        while True:
            try:
                return self.put_nowait(obj)
            except self.Full:
                if timeout is not None:
                    lasted = time.time() - start_time
                    if timeout > lasted:
                        time.sleep(min(self.max_timeout, timeout - lasted))
                    else:
                        raise RuntimeError("timeout is too short!")
                else:
                    time.sleep(self.max_timeout)

    def get_nowait(self):
        """非等待获取"""
        ret = self.redis.lpop(self.name)
        if ret is None:
            raise self.Empty
        return pickle.loads(ret)

    def get(self, block=True, timeout=None):
        """等待获取"""
        if block is not True:
            return self.get_nowait()

        start_time = time.time()
        while True:
            try:
                return self.get_nowait()
            except self.Empty:
                if timeout is not None:
                    lasted = time.time() - start_time
                    if timeout > lasted:
                        time.sleep(min(self.max_timeout, timeout - lasted))
                    else:
                        raise RuntimeError("timeout is too short!")
                else:
                    time.sleep(self.max_timeout)
