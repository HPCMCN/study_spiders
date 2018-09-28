# -*- coding: utf-8 -*-
import scrapy

from ..items import TencentItem


class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['hr.tencent.com']
    base_url = "https://hr.tencent.com/position.php?&start="
    offset = 0
    start_urls = [base_url + str(offset)]

    def parse(self, response):
        node_list = response.xpath("//*[@class='even'] | //*[@class='odd']")
        for node in node_list:
            item = TencentItem()
            item["position_name"] = node.xpath("./td[1]/text()").extract_first()
            item["position_link"] = "http://hr.tencent.com/" + node.xpath("./td[1]/a/@href").extract_first()
            item["position_type"] = node.xpath("./td[2]/text()").extract_first()
            item["people_number"] = node.xpath("./td[3]/text()").extract_first()
            item["work_location"] = node.xpath("./td[4]/text()").extract_first()
            item["publish_times"] = node.xpath("./td[5]/text()").extract_first()

            yield scrapy.Request(item["position_link"], meta={"item": item}, callback=self.parse_detail)

        if response.xpath("//a[@id='next' and @class='noative']/@href").extract_first() is None:
            next_url = "https://hr.tencent.com/" + response.xpath("//a[@id='next']/@href").extract_first()
            yield scrapy.Request(next_url, callback=self.parse)

    def parse_detail(self, response):
        item = response.meta["item"]
        item["position_duty"] = response.xpath("//ul[@class='squareli']")[0].xpath("./li/text()").extract()
        item["position_requirement"] = response.xpath("//ul[@class='squareli']")[1].xpath("./li/text()").extract()
        return item
