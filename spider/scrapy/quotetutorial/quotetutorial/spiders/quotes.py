# -*- coding: utf-8 -*-
import scrapy
from ..items import QuotetutorialItem

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css('.quote')
        for quote in quotes:
            item = QuotetutorialItem()
            text = quote.css('.text::text').extract_first()
            name = quote.css('.author::text').extract_first()
            tags = quote.css('.tag::text').extract()
            item['text'] = text
            item['name'] = name
            item['tags'] = tags
            yield item
        next = response.css('nav > ul > li.next > a::attr(href)').extract_first()
        url = response.urljoin(next)
        yield scrapy.Request(url=url,callback=self.parse)

