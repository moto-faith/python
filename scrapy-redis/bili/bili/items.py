# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BiliItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # mid name sex face sign level following follower
    mid = scrapy.Field()
    name = scrapy.Field()
    sex = scrapy.Field()
    face = scrapy.Field()
    sign = scrapy.Field()
    level = scrapy.Field()
    following = scrapy.Field()
    follower = scrapy.Field()
