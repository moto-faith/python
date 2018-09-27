# -*- coding: utf-8 -*-
import scrapy
from ..items import WeatherItem

import re

base_url = 'https://www.aqistudy.cn/historydata/'
class AqistudySpider(scrapy.Spider):
    name = "aqistudy"
    allowed_domains = ["www.aqistudy.cn/historydata"]
    start_urls = ['https://www.aqistudy.cn/historydata/']


    def parse(self, response):

        city_list = response.xpath('//div[@class="all"]//div[@class="bottom"]//a//@href').extract_first()
        # for city in city_list:
        city_url = response.urljoin(city_list)

        request = scrapy.Request(url=city_url,callback=self.month, dont_filter=True)
        yield request

    def month(self,response):
        response = response.text
        month_list = re.findall('<li><a href="(.*?)">',response,re.S)



        for month in month_list:
            days = base_url+month
            request = scrapy.Request(days,callback=self.day, dont_filter=True)
            yield request

    def day(self,response):

        item = WeatherItem()
        item['city'] = re.findall('<h2 id="title">.*?月(.*?)空气质量指数日历史数据</h2>', response.text, re.S)

        day_list = response.xpath('//table[@class="table table-condensed table-bordered table-striped table-hover table-responsive"]//tr')
        for i, date_data in enumerate(day_list):
            if i==0:
                continue
            print(item['city'],i)
            td_list = date_data.xpath('.//td')
            item['city'] = re.findall('<h2 id="title">.*?月(.*?)空气质量指数日历史数据</h2>',response.text,re.S)
            print(item['city'])
            item['date'] = td_list[0].xpath('text()').extract_first()            # 检测日期
            item['aqi'] = td_list[1].xpath('text()').extract_first()                # AQI

            item['zhiliang'] = td_list[2].xpath('./span/text()').extract_first()              # 质量
            item['pm25'] = td_list[3].xpath('text()').extract_first()              # PM2.5
            item['pm10'] = td_list[4].xpath('text()').extract_first()               # PM10
            item['so2'] = td_list[5].xpath('text()').extract_first()                # SO2
            item['co'] = td_list[6].xpath('text()').extract_first()                 # CO
            item['no2'] = td_list[7].xpath('text()').extract_first()                # NO2
            item['o3_8h'] = td_list[8].xpath('text()').extract_first()                 # O3
            yield item


