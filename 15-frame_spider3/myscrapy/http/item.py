#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Power by HPCM   2018-09-27 15:06:27


class Item(object):
    """数据提供接口"""

    def __init__(self, data):
        self._item_data = data

    @property
    def data(self):
        return self._item_data
