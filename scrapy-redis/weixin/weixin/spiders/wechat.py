# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
import requests
import random
import json
import time


# https://mp.weixin.qq.com/cgi-bin/searchbiz?begin=0&count=5&action=search_biz&lang=zh_CN&random=0.2817618625761683&token=1200684770&f=json&ajax=1&query=%E8%8B%B9%E6%9E%9C
class WechatSpider(scrapy.Spider):
    name = "wechat"
    allowed_domains = ["weixin.sogou.com"]

    token = '2141309833'
    word = '苹果'
    cookie = {
        'noticeLoginFlag': '1',
        'pgv_pvid': '1165112528',
        'pac_uid': '0_5b63c7fb0cb76',
        'pgv_pvi': '7421473792',
        'ptui_loginuin': '1064030249',
        'pt2gguin': 'o1064030249',
        'RK': 'JaZZJTZ1bH',
        'ptcz': '6e0a25cb6c39e209a52346a2ccba707087f9aaee828cac6695329b3caea9b631',
        'o_cookie': '1064030249',
        'tvfe_boss_uuid': '30cf055eeda6c090',
        'mobileUV': '1_165ddbfdd88_9b142',
        '_ga': 'GA1.2.1106076095.1538867647',
        'ua_id': 'r6gh2o9mLyiGTjM5AAAAAEF2ryMVt68FeW0oA4vp2w8=',
        'mm_lang': 'zh_CN',
        'pgv_si': 's1417620480',
        'cert': 'FN4ppQ_lOjhISVw5x6_3hZoMe7vSL3SN',
        'sig': 'h0137a2d6f2d716e669644860abfc2bd99b181cedf01b0d9607ede72408f180f654d92ce65f9852a9d8',
        'uuid': 'e2eea8f83023526f4ba15628df1403b3',
        'bizuin': '3594738754',
        'ticket': '5a96bbea4c501f0bcdb4d17fb01c8df516079321',
        'ticket_id': 'gh_652fd68b1fb0',
        'data_bizuin': '3594738754',
        'data_ticket': 'X/6qzHQNYw2GyUHU+SSXDWImv6rwvrxeerzDodlegkMvpnrKJf+xvUoKcM77dbFA',
        'slave_sid': 'MnN1Q2RwQ3ZlMDlIZDEza3lId0p0TTBNWjNyUkdyUVp4c0I1Nm1MZDVQWk50U3dpVU5NZVBZTmFoM3JlTVBuSEhNdjF5dFd0bUk5T0s3Z1BhNnlBZm1ycHJBQnNkRjRsSG52ajVCdWhUbDd5SktDT1lKYVlMcGhIMXk4ZWo1QnE4QlQ1c3VsRklOWmdDWEJp',
        'slave_user': 'gh_652fd68b1fb0',
        'xid': '73d2a07f0832eb5de0dddc715ad7052d',
        'openid2ticket_oQlxD1m0OOYuiqAPrUEFfLoLJIOE': 'jsva4+wzY6vhjtfitEtaSwkAU2aZk34z8SKO3D7jEyM='

    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
        'Connection': 'keep-alive',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }

    def start_requests(self):
        # 搜索微信公众号接口需要传入的参数，有三个变量：微信公众号token、随机数random、搜索的微信公众号名字
        for i in range(0, 5, 5):  # 这里循环的是公众号数量

            start_urls = 'https://mp.weixin.qq.com/cgi-bin/searchbiz?begin={}&count=5&action=search_biz&lang=zh_CN&random={}&token={}&f=json&ajax=1&query={}'.format(
                i, random.random(), self.token, self.word)
            # 打开搜索微信公众号接口地址，需要传入相关参数信息如：cookies、params、headers
            yield Request(start_urls, cookies=self.cookie, headers=self.headers, callback=self.parse)

    def parse(self, response):
        # 取搜索结果中的第一个公众号
        lists = json.loads(response.text)["list"]
        # 获取这个公众号的fakeid，后面爬取公众号文章需要此字段
        fakeids = [list["fakeid"] for list in lists]
        print(fakeids)
        for fakeid in fakeids:  # 遍历每个公众号
            for k in range(0, 5, 5):  # 遍历该公众号内所有文章
                url = 'https://mp.weixin.qq.com/cgi-bin/appmsg?token={}&lang=zh_CN&f=json&ajax=1&random=0.578791056424645&action=list_ex&begin={}&count=5&query=&fakeid={}&type=9'.format(
                    self.token, k, fakeid)
                r = requests.get(url=url, headers=self.headers, cookies=self.cookie).text
                list = json.loads(r)["app_msg_list"]
                for i in list:
                    print(i["title"])
                    print(i["link"])
                    print(time.localtime(i["update_time"]))
