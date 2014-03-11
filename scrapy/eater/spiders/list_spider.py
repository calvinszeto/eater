from scrapy.spider import Spider
from scrapy.selector import Selector

from eater.items import RestaurantItem

class ListSpider(Spider):
    name = "list"
    allowed_domains = ["eater.com"]
    start_urls = [
        "http://localhost:8050/render.html?url=http://houston.eater.com/archives/2014/01/07/the-essential-38-houston-restaurants-january-2014-1.php&timeout=10&wait=0.5"
    ]

    def parse(self, response):
        sel = Selector(response)
        restaurants = sel.xpath('//div[@class="point-mode point-mode-list"]/div/div')
        items = []
        for restaurant in restaurants:
            item = RestaurantItem()
            name = restaurant.xpath('div[@class="name fn org overflow-controlled"]/@title').extract()
            address = restaurant.xpath('div[@class="metadata"]/div[@class="address adr overflow-controlled"]/text()').extract()
            website = restaurant.xpath('div[@class="metadata"]/div[@class="url overflow-controlled"]/a/@href').extract()
            item['name'] = name[0] if name else ""
            item['address'] = address[0] if address else ""
            item['website'] = website[0] if website else ""
            items.append(item)
        return items
