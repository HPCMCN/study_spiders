#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Power by HPCM   2018-09-28 22:20:04

DEFAULT_LOG_FILENAME = "baidu.log"

SPIDERS = [
        "baidu.BaiduSpider",
        # "spiders.douban.DoubanSpider"
        ]

PIPELINES = [
        "pipeline.BaiduPipeline",
        # "pipelines.DoubanPipeline"
        ]

SPIDER_MIDDLEWARES = [
        "middlewares.SpiderMiddleware",
        "middlewares.SpiderMiddleware"
        ]

DOWNLOAD_MINDDLEWARES = [
        "middlewares.DownloadMiddleware",
        ]
