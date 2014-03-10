from scrapy.spider import Spider
from scrapy.selector import Selector

class ListSpider(Spider):
    name = "list"
    allowed_domains = ["eater.com"]
    start_urls = [
        "http://localhost:8050/render.html?url=http://houston.eater.com/archives/2014/01/07/the-essential-38-houston-restaurants-january-2014-1.php&timeout=10&wait=0.5"
    ]

    def parse(self, response):
        sel = Selector(response)
        restaurants = sel.xpath('//div[@class="point-mode point-mode-list"]/div/div')
        for restaurant in restaurants:
            name = restaurant.xpath('div[@class="name fn org overflow-controlled"]/@title').extract()
            address = restaurant.xpath('div[@class="metadata"]/div[@class="address adr overflow-controlled"]/text()').extract()
            website = restaurant.xpath('div[@class="metadata"]/div[@class="url overflow-controlled"]/a/@href').extract()
            print name, address, website
