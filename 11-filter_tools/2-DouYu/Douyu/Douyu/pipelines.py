# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
import scrapy
from scrapy.pipelines.images import ImagesPipeline
from .settings import IMAGES_STORE
class DouyuImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield scrapy.Request(item["image_url"])

    def item_completed(self, results, item, info):
        old_name = IMAGES_STORE + [x["path"] for ok, x in results if ok][0]
        try:
            item["image_path"] = new_name = IMAGES_STORE + item["nick_name"].replace("/", "-") + ".jpg"
            os.rename(old_name, new_name)
        except OSError:
            pass
        return item

