# -*- coding: utf-8 -*-
import scrapy
from ..items import ClassItem
from scrapy.http import Request

class CourseSpider(scrapy.Spider):
    name = "course"
    allowed_domains = ["edu.hellobi.com"]
    start_urls = ['https://edu.hellobi.com/course/1']

    def parse(self, response):
        i = ClassItem()
        i['name'] = response.xpath('//li[@class="active"]/text()').extract()
        i['url'] = response.xpath('//li[@role="presentation"]/a/@href').extract()
        i['num'] = response.xpath('//span[@class="course-view"]/text()').extract()
        yield i
        for i in range(2,295):
            url = 'https://edu.hellobi.com/course/'+str(i)
            yield Request(url,callback=self.parse)
