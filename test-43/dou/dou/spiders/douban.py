# -*- coding: utf-8 -*-
import scrapy
from ..items import DouItem
from scrapy.http import Request,FormRequest
from urllib.request import urlretrieve

class DoubanSpider(scrapy.Spider):
    name = "douban"
    allowed_domains = ["douban.com"]
    # start_urls = ['http://douban.com/']
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    def start_requests(self):
        return [Request('https://accounts.douban.com/login',headers=self.headers,meta={'cookiejar':1},callback=self.parse)]
    def parse(self, response):
        img = response.xpath('//img[@id="captcha_image"]/@src').extract()
        if len(img)>0:
            print('验证码登陆中,请查看验证码')
            urlretrieve(img[0],'captcha.png')
            print('请输入验证码')
            captcha = input()
            url = 'https://accounts.douban.com/login'
            data = {
                "form_email": '111111111111',
                "form_password": '22222222222',
                "redir": 'https://www.douban.com/people/333333333/',
                "captcha-solution":captcha
            }

            return [FormRequest.from_response(response, meta={'cookiejar': response.meta['cookiejar']},
                                              headers=self.headers, formdata=data, callback=self.next)]
        else:

            url = 'https://accounts.douban.com/login'
            data = {
                "form_email":'11111111111',
                "form_password":'222222222222222',
                "redir":'https://www.douban.com/people/33333333333/'
            }
            print('无验证码登陆中')
            return [FormRequest.from_response(response,meta = {'cookiejar':response.meta['cookiejar']},
                                             headers = self.headers,formdata=data,callback = self.next)]

    def next(self,response):
        i=DouItem()
        print('登陆成功')
        i['name'] = response.xpath('//title/text()').extract()
        i['title'] = response.xpath('//div[@class="note-header pl2"]/a/text()').extract()
        i['content'] = response.xpath('//div[@class="note"]/text()').extract()
        yield i
