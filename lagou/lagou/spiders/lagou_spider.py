# -*- coding: utf-8 -*-
import scrapy
from lagou.items import LagouItem


class LagouSpiderSpider(scrapy.Spider):
    name = 'lagou_spider'
    allowed_domains = ['lagou.com']
    start_urls = [
        'https://www.lagou.com/zhaopin/Python/{}/?filterOption=3'.format(i) for i in range(1, 31)
    ]

    def parse(self, response):
        item = LagouItem()
        divs = response.xpath('//*[@id="s_position_list"]/ul/li/div[1]')
        for div in divs:
            title = div.xpath('./div[1]/div[1]/a/h3/text()').extract()
            address = div.xpath('./div[1]/div[1]/a/span/em/text()').extract()
            money = div.xpath('./div[1]/div[2]/div/span/text()').extract()
            company = div.xpath('./div[2]/div[1]/a/text()').extract()
            fintance = div.xpath('./div[2]/div[2]/text()').extract()

            job_title = title[0] if len(title) > 0 else '无数据'
            job_address = address[0] if len(address) > 0 else '无数据'
            job_money = money[0] if len(money) > 0 else '无数据'
            job_company = company[0] if len(company) > 0 else '无数据'
            job_fintance = fintance[0] if len(fintance) > 0 else '无数据'

            item['title'] = job_title.strip()
            item['address'] = job_address.strip()
            item['money'] = job_money.strip()
            item['company'] = job_company.strip()
            item['fintance'] = job_fintance.strip()

            yield item

