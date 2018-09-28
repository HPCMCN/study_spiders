#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Power by HPCM   2018-09-27 15:39:27
from datetime import datetime

from .spider import Spider
from .scheduler import Scheduler
from .download import Download
from .pipeline import Pipeline
from ..http.item import Item
from ..http.request import Request

from ..utils.logger import logger

class Engine(object):
    """引擎, 中心调度"""
    def __init__(self):
        self.spider = Spider()
        self.scheduler = Scheduler()
        self.download = Download()
        self.pipeline = Pipeline()

    def main(self):
        # 获取获取请求
        start_request = self.spider.start_request()
        # 请求入列, 判重
        self.scheduler.add_request(start_request)
        # 取出队列中的url
        request = self.scheduler.get_request()
        # 发送请求获取响应
        response = self.download.send_request(request)
        # 解析数据
        result = self.spider.parse(response)
        # 判断解析后的数据是url, 还是data:
        if isinstance(result, Request):
            self.scheduler.add_request(result)
        elif isinstance(result, Item):
            self.pipeline.process_item(result)

    def start(self):
        start = datetime.now()
        logger.info("Start time is [ {} ]".format(start))
        self.main()
        end = datetime.now()
        logger.info("End time is [ {} ]".format(end))
        print("[INFO]: run time is {}s".format((end - start).total_seconds()))
