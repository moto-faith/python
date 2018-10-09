# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import requests
import json
import random

class HttpbinProxyMiddleware(object):

    def __init__(self):
        self.count = 1# 可以用来计数，让一个代理用多少回后丢弃
        self.ip = 0
        self.port = 0


    def process_request(self, request, spider):

        if self.count==1 or self.count%100==0:# 每10000次换一个代理
            pro_addr = requests.get('http://127.0.0.1:8000/?protocol=1&country=国内').text
            ip_ports = json.loads(pro_addr)
            ips = random.choice(ip_ports)# 每次的代理都不相同
            self.ip,self.port = self.check(ips)
        else:
            self.ip= self.ip
            self.port =self.port

        print('此次的ip:',self.ip)
        request.meta['proxy'] = 'http://{}:{}'.format(self.ip,self.port)
        self.count+=1

    def check(self, ips):
        ip = ips[0]
        port = ips[1]
        proxies={
            'http':'http://%s:%s'%(ip,port),
            'https':'http://%s:%s'%(ip,port)
        }
        r=requests.get('https://api.bilibili.com/x/space/app/index?mid=1',proxies = proxies,timeout = 3)# 验证是否能联通目标服务器
        while r.status_code!=200:
            pro_addr = requests.get('http://127.0.0.1:8000/?protocol=1&country=国内').text
            ip_ports = json.loads(pro_addr)
            ips = random.choice(ip_ports)  # 每次的代理都不相同
            self.check(ips)
        self.ip, self.port = ip,port
        return self.ip,self.port




class BiliSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
