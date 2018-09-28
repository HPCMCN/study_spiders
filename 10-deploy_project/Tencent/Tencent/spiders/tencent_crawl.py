#coding: utf-8
import scrapy

from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import TencentItem, PositionItem


class TencentSpider(CrawlSpider):
    """"""
    name = "tencent_crawl"
    allowed_domains = ["hr.tencent.com"]
    start_urls = ["https://hr.tencent.com/position.php?&start=0#"]

    rules = [
        Rule(LinkExtractor(allow=r"position\.php\?&strart=\d+"), callback="parse_item", follow=True),
        Rule(LinkExtractor(allow=r"php\?id=\d+"), callback="parse_detail", follow=False),
    ]

    def parse_item(self, response):
        node_list = response.xpath("//*[@class='even'] | //*[@class='odd']")
        for node in node_list:
            item = TencentItem()
            item["position_name"] = node.xpath("./td[1]/text()").extract_first()
            item["position_link"] = u"http://hr.tencent.com/" + node.xpath("./td[1]/a/@href").extract_first()
            item["position_type"] = node.xpath("./td[2]/text()").extract_first()
            item["people_number"] = node.xpath("./td[3]/text()").extract_first()
            item["work_location"] = node.xpath("./td[4]/text()").extract_first()
            item["publish_times"] = node.xpath("./td[5]/text()").extract_first()

            yield item

    def parse_detail(self, response):
        item = PositionItem()
        item["position_duty"] = response.xpath("//ul[@class='squareli']")[0].xpath("./li/text()").extract()
        item["position_requirement"] = response.xpath("//ul[@class='squareli']")[1].xpath("./li/text()").extract()
        yield item
