#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Power by HPCM   2018-09-28 22:20:04

DEFAULT_LOG_FILENAME = "baidu.log"

SPIDERS = [
        "baidu.BaiduSpider",
        "Douban.DoubanSpider"
        ]

PIPELINES = [
        "pipeline.BaiduPipeline",
        "pipeline.DoubanPipeline"
        ]

SPIDER_MIDDLEWARES = [
        #"middlewares.SpiderMiddleware",
        "middlewares.SpiderMiddleware"
        ]

DOWNLOAD_MINDDLEWARES = [
        # "middlewares.DownloadMiddleware",
        ]


# ASYNC_TYPE = "thread"
ASYNC_TYPE = "coroutine"
ASYNC_COUNT = 10
TIME_SLEEP = 0.01

# ROLE = None
ROLE = "mater"
# ROLE = "slave"
