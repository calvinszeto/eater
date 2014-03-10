from scrapy.spider import Spider

class ListSpider(Spider):
    name = "list"
    allowed_domains = ["eater.com"]
    start_urls = [
        "http://houston.eater.com/archives/2014/01/07/the-essential-38-houston-restaurants-january-2014-1.php"
    ]

    def parse(self, response):
       filename = response.url.split("/")[-2] 
       open(filename, 'wb').write(response.body)
