#!/usr/bin/env python
#-*- coding:utf-8 -*-
# Power by HPCM   2018-09-27 15:36:59


class Pipeline(object):
    """数据保存"""
    def process_item(self, item):
        print("[INFO]: pipeline.process_item: {}".format(item.data["url"]))


