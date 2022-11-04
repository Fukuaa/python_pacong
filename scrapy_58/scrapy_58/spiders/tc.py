import scrapy


class TcSpider(scrapy.Spider):
    name = 'tc'
    allowed_domains = ['https://www.autohome.com.cn/series/mLnqRyEiBWM']
    start_urls = ['https://www.autohome.com.cn/series/mLnqRyEiBWM']

    def parse(self, response):
        price_list = response.xpath('//div[@class="guidance-price__con"]/span/text()')
        name_list = response.xpath('//div[@class="spec-name"]/div/p/a/text()')
        for i in range(len(name_list)):
            name = name_list[i].extract()
            price = price_list[i].extract()
            print(name, price)
