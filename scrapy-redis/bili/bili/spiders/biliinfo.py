# -*- coding: utf-8 -*-
import scrapy
from ..items import BiliItem
import json
from scrapy.http import Request
import re
from scrapy_redis.spiders import RedisCrawlSpider

class BiliinfoSpider(RedisCrawlSpider):
    name = "biliinfo"
    allowed_domains = ["bilibili.com"]
    redis_key = "spider:start_urls"
    # start_urls = ['https://api.bilibili.com/x/space/app/index?mid=1']

    def parse(self,response):
        i = BiliItem()
        r = response.text
        data = json.loads(r)
        info = data["data"]["info"]
        i["mid"] = info["mid"]
        i["name"] = info["name"]
        i["sex"] = info["sex"]
        i["face"] = info["face"]
        i["sign"] = info["sign"]
        i["level"] = info["level"]
        i["following"] = info["following"]
        i["follower"] = info["follower"]
        yield i

        for k in range(450000, 999999999):
            yield Request(url='https://api.bilibili.com/x/space/app/index?mid={}'.format(k), callback=self.main)

    def main(self, response):
        i=BiliItem()
        r = response.text
        data = json.loads(r)

        if data["code"]==0:
            info = data["data"]["info"]
            if info["name"]=="bilibili":
                pass
            else:
                i["mid"]=info["mid"]
                i["name"]=info["name"]
                i["sex"]=info["sex"]
                i["face"]=info["face"]
                i["sign"]=info["sign"]
                i["level"]=info["level"]
                i["following"]=info["following"]
                i["follower"]=info["follower"]
                yield i

        else:
             pass


