# -*- coding: utf-8 -*-
import scrapy
from ..items import DangItem
from scrapy.http import Request

class DangdangSpider(scrapy.Spider):
    name = "dangdang"
    allowed_domains = ["dangdang.com"]
    start_urls = ['http://category.dangdang.com/cp01.54.06.00.00.00.html']

    def parse(self, response):
        i=DangItem()
        i['name'] = response.xpath('//a[@dd_name="单品标题"]/text()').extract()
        i['num'] = response.xpath('//a[@dd_name="单品评论"]/text()').extract()
        i['price'] = response.xpath('//span[@class="search_now_price"]/text()').extract()
        yield i
        for i in range(2,11):
            url = 'http://category.dangdang.com/pg{}-cp01.54.06.00.00.00.html'.format(i)
            yield Request(url,callback=self.parse)


