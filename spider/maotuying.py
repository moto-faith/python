#!/usr/bin/env python
# -*- encoding: utf-8 -*-
# Created on 2018-09-21 14:37:19
# Project: demo

#pyspider all
#localhost:5000

from pyspider.libs.base_handler import *
import pymongo


class Handler(BaseHandler):
    crawl_config = {
    }
    client = pymongo.MongoClient('localhost')
    db = client['trip']

    @every(minutes=24 * 60)
    def on_start(self):
        self.crawl(
            'https://www.tripadvisor.cn/Attractions-g186338-Activities-c47-oa30-London_England.html#FILTERED_LIST',
            callback=self.index_page)

    @config(age=10 * 24 * 60 * 60)
    def index_page(self, response):
        for each in response.doc(' div.listing_info > div.listing_title > a').items():
            self.crawl(each.attr.href, callback=self.detail_page)
        next = response.doc('div > a.nav.next.rndBtn.ui_button.primary.taLnk').attr.href
        self.crawl(next, callback=self.index_page)

    @config(priority=2)
    def detail_page(self, response):
        name = response.doc('#HEADING').text()
        rating = response.doc('div > div.ratingContainer > a > span').text().replace('\xa0', '')
        address = response.doc(
            'div.prw_rup.prw_common_atf_header_bl_responsive.headerBL > div > div > span.detail').text()
        phone = response.doc('div.contact > div.contactType.phone.is-hidden-mobile > div').text()
        return {
            "url": response.url,
            'name': name,
            'rating': rating,
            'address': address,
            'phone': phone

        }

    def on_result(self, result):
        if result:
            self.save_to_mongo(result)

    def save_to_mongo(self, result):
        if self.db['london'].insert(result):
            print('saved to mongo', result)