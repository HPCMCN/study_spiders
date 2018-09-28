#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Power by HPCM   2018-09-27 16:52:29

import logging

DEFAULT_LOG_LEVEL = logging.INFO
DEFAULT_LOG_FMT = "%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s:%(message)s"
DEFAULT_LOG_DATEFMT = "%Y-%m-%d %H:%M:%S"
DEFAULT_LOG_FILENAME = "log.txt"
print("导入成功!")
try:
    from setting import *
except ImportError:
    print("抛出异常!")
    pass

