#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Power by HPCM   2018-09-27 16:52:29

import logging

DEFAULT_LOG_LEVEL = logging.INFO
# noinspection SpellCheckingInspection
DEFAULT_LOG_FMT = "%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s:%(message)s"
# noinspection SpellCheckingInspection
DEFAULT_LOG_DATEFMT = "%Y-%m-%d %H:%M:%S"
DEFAULT_LOG_FILENAME = "log.txt"

# 异步类型
# noinspection SpellCheckingInspection
ASYNC_TYPE = "coroutine"
# 开启个数
ASYNC_COUNT = 10
# 轮寻等待时间
TIME_SLEEP = 0.1

# 爬虫分布式
ROLE = None
# ROLE = "mater"
# ROLE = "slave"

# 接口兼容 redis_queue
REDIS_QUEUE_NAME = "request_queue"
REDIS_QUEUE_HOST = "127.0.0.1"
REDIS_QUEUE_PORT = "6379"
REDIS_QUEUE_DB = 9

# 接口兼容 redis_set
REDIS_SET_NAME = "set"
REDIS_SET_HOST = "127.0.0.1"
REDIS_SET_PORT = "6379"
REDIS_SET_DB = 11
try:
    # noinspection PyPackageRequirements
    from setting import *

    print("导入成功!")
except ImportError:
    print("抛出异常!")
    pass
