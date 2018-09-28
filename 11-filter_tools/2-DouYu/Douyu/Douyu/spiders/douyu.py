# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import DouyuItem

class DouyuSpider(scrapy.Spider):
    name = 'douyu2'
    base_url = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=100&offset="
    offset = 0
    start_urls = [base_url + str(offset)]

    def parse(self, response):
        data_list = json.loads(response.body)["data"]
        if not data_list:
            return
        for data in data_list:
            item = DouyuItem()
            item["room_url"] = data["room_id"]
            item["image_url"] = data["vertical_src"]
            item["nick_name"] = data["nickname"]
            item["online"] = data["online"]
            item["city"] = data["anchor_city"]
            
            yield item
        
        self.offset += 100
        yield scrapy.Request(self.base_url + str(self.offset), callback=self.parse)

