#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Power by HPCM   2018-09-27 16:20:47
# import sys

import sys
from ..config.default_setting import *

class Logger(object):
    """日志系统"""

    def __init__(self):
        # 获取log对象
        self._logger = logging.getLogger()
        # 设置格式化对象format
        self.formatter = logging.Formatter(fmt=DEFAULT_LOG_FMT, datefmt=DEFAULT_LOG_DATEFMT)
        # 设置日志模式输出方式, 日志模式和终端模式
        self._logger.addHandler(self._get_file_handler(DEFAULT_LOG_FILENAME))
        self._logger.addHandler(self._get_console_handler())
        # 设置日志等级
        self._logger.setLevel(DEFAULT_LOG_LEVEL)

    def _get_file_handler(self, filename):
        """生成hanhler对象"""
        filehandler = logging.FileHandler(filename=filename)
        filehandler.setFormatter(self.formatter)
        return filehandler

    def _get_console_handler(self):
        """生成命令行日志对象"""
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setFormatter(self.formatter)
        return console_handler

    @property
    def logger(self):
        return self._logger


logger = Logger().logger
