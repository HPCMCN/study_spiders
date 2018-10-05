#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Power by HPCM   2018-09-27 15:39:27
from datetime import datetime

from .scheduler import Scheduler
from .download import Download
from ..http.item import Item
from ..http.request import Request

from ..utils.logger import *
from myscrapy.core.spider import Spider


class Engine(object):
    """引擎, 中心调度"""

    def __init__(self):
        # 爬虫
        self.spiders = self.auto_import_module(SPIDERS)
        # 调度
        self.scheduler = Scheduler()
        # 响应
        self.download = Download()
        # 保存
        self.pipelines = self.auto_import_module(PIPELINES)

        # 爬虫中间件/下载中间件
        self.spider_mids = self.auto_import_module(SPIDER_MIDDLEWARES)
        self.download_mids = self.auto_import_module(DOWNLOAD_MINDDLEWARES)

    def main(self):
        # 遍历爬虫列表
        for spider_name, spider in self.spiders.items():
            # 获取获取请求
            for start_request in spider.start_requests():
                # url入队列之前预处理, spider中间件
                start_request.name = spider_name
                for spider_mid in self.spider_mids:
                    start_request = spider_mid.process_request(start_request)
                # 请求入列, 判重
                self.scheduler.add_request(start_request)

        while True:
            # 取出队列中的url
            request = self.scheduler.get_request()
            if request is None:
                break
            # 请求之前预处理, download中间件
            for download in self.download_mids:
                request = download.process_request(request)
            # 发送请求获取响应
            response = self.download.send_request(request)
            # 响应之后处理, download中间件
            for download in self.download_mids:
                response = download.process_response(response)
            # 解析数据
            spider = self.spiders[request.name]
            result = spider.parse(response)
            # 判断解析后的数据是url, 还是data:
            if isinstance(result, Request):
                # url入队列之前预处理, spider中间件
                result.spider_name = request.spider_name
                for spider_mid in self.spider_mids:
                    result = spider_mid.process_request(result)
                # 继续解析url
                self.scheduler.add_request(result)
            elif isinstance(result, Item):
                # 保存之前预处理
                for spider_mid in self.spider_mids:
                    result = spider_mid.process_item(result)
                # 保存response
                for pipeline in self.pipelines:
                    pipeline.process_item(result, spider)

    def start(self):
        start = datetime.now()
        logger.info("Start time is [ {} ]".format(start))
        self.main()
        end = datetime.now()
        logger.info("End time is [ {} ]".format(end))
        print("[INFO]: run time is {}s".format((end - start).total_seconds()))

    @staticmethod
    def auto_import_module(module_list):
        instance = {}
        instance1 = []
        for module in module_list:
            index = module.rfind(".")
            # 遍历并拆分变量名, path_name: 路径, var_name: 变量名
            path_name = module[:index]
            var_name = module[index + 1:]
            # 动态导入模块
            import_module = __import__(path_name)
            # 动态导入变量
            var = getattr(import_module, var_name)
            # 判断是否有tag属性, 并且属性为spider, 则为spider, 进行实例化
            if hasattr(var, "tag") and var.tag == "spider":
                instance[var.name] = var()
            else:
                instance1.append(var())
        return instance or instance1
