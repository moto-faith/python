# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request
from ..items import BookItem
from scrapy_redis.spiders import RedisCrawlSpider


class DangSpider(RedisCrawlSpider):
    name = "dang"
    allowed_domains = ["dangdang.com"]
    redis_key = "myspider:start_urls"
    # start_urls = ['http://category.dangdang.com/cp01.00.00.00.00.00-shbig.html']

    def parse(self, response):
        tags = response.xpath('//div[@class="clearfix"]/span/a/@href').extract()
        for tag in tags:

            isbig = re.findall('/(.*?-sh)big.html',tag)
            if isbig:
                for i in range(1,101):
                    url = 'http://category.dangdang.com/pg{}-'.format(i) + isbig[0]+'list.html'
                    yield Request(url=url,callback=self.listbook)

            else:
                for i in range(1, 101):
                    url = 'http://category.dangdang.com/pg{}-'.format(i)+tag[1:]
                    yield Request(url=url,callback=self.listbook)

    def listbook(self,response):
        i = BookItem()
        url = response.xpath('//a[@dd_name="单品标题"]/@href').extract()
        name = response.xpath('//a[@dd_name="单品标题"]/text()').extract()
        price = response.xpath('//span[@class="search_now_price"]/text()').extract()
        company = response.xpath('//a[@dd_name="单品出版社"]/text()').extract()
        comment = response.xpath('//a[@dd_name="单品评论"]/text()').extract()
        date = response.xpath('//p[@class="search_book_author"]/span[2]/text()').extract()
        for i['url'],i['name'],i['price'],i['company'],i['comment'],i['date'] in zip(url,name,price,company,comment,date):
            yield i




