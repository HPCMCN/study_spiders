# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuItem(scrapy.Item):
    # define the fields for your item here like:
    room_url = scrapy.Field()
    image_url = scrapy.Field()
    nick_name = scrapy.Field()
    online = scrapy.Field()
    city = scrapy.Field()
    image_path = scrapy.Field()
