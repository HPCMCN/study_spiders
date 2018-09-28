# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # 职位
    position_name = scrapy.Field()
    position_link = scrapy.Field()
    position_type = scrapy.Field()
    people_number = scrapy.Field()
    work_location = scrapy.Field()
    publish_times = scrapy.Field()
    position_duty = scrapy.Field()
    position_requirement = scrapy.Field()
    time = scrapy.Field()
    source = scrapy.Field()

class PositionItem(scrapy.Item):
    # define the fields for your item here like:
    # 职位
    position_duty = scrapy.Field()
    position_requirement = scrapy.Field()
