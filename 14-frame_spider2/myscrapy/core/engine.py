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

from ..middlewares.spider_middlewares import SpiderMiddleware
from ..middlewares.download_middlewares import DownloadMiddleware

from ..utils.logger import logger

class Engine(object):
    """引擎, 中心调度"""
    def __init__(self):
        # 爬虫
        self.spider = Spider()
        # 调度
        self.scheduler = Scheduler()
        # 响应
        self.download = Download()
        # 保存
        self.pipeline = Pipeline()

        # 爬虫中间件/下载中间件
        self.spider_mid = SpiderMiddleware()
        self.download_mid = DownloadMiddleware()

    def main(self):
        # 获取获取请求
        for start_request in self.spider.start_requests():
            # url入队列之前预处理, spider中间件
            start_request = self.spider_mid.process_request(start_request)
            # 请求入列, 判重
            self.scheduler.add_request(start_request)

        while True:
            # 取出队列中的url
            request = self.scheduler.get_request()
            if request is None:
                break
            # 请求之前预处理, download中间件
            request = self.download_mid.process_request(request)
            # 发送请求获取响应
            response = self.download.send_request(request)
            # 响应之后处理, download中间件
            response = self.download_mid.process_response(response)
            # 解析数据
            result = self.spider.parse(response)
            # 判断解析后的数据是url, 还是data:
            if isinstance(result, Request):
                # url入队列之前预处理, spider中间件
                start_request = self.spider_mid.process_request(start_request)
                # 继续解析url
                self.scheduler.add_request(result)
            elif isinstance(result, Item):
                # 保存之前预处理
                result = self.spider_mid.process_item(result)
                # 保存response
                self.pipeline.process_item(result)

    def start(self):
        start = datetime.now()
        logger.info("Start time is [ {} ]".format(start))
        self.main()
        end = datetime.now()
        logger.info("End time is [ {} ]".format(end))
        print("[INFO]: run time is {}s".format((end - start).total_seconds()))
