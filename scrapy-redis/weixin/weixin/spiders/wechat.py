# -*- coding: utf-8 -*-
import scrapy


class WechatSpider(scrapy.Spider):
    name = "wechat"
    allowed_domains = ["weixin.sogou.com"]
    start_urls = 'https://weixin.sogou.com/weixin?query=%E8%8B%B9%E6%9E%9C&type=2&page=12&ie=utf8'
    def parse(self, response):
        title = response.xpath('//div[@class="txt-box"]/h3/a/text()').extract()
        url = response.xpath('//div[@class="txt-box"]/h3/a/@href').extract()
        print(title, url,response.text)
