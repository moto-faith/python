#encoding='utf-8'
import requests
from lxml import etree
import re
import json
import sys



headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
r = requests.get('http://top.baidu.com/boards?fr=topcategory_c513',headers=headers).text
se = etree.HTML(r)
urls = se.xpath('//div[@class="main"]//div[@class="links"]/a/@href')
for url in urls:
    r = requests.get('http://top.baidu.com/{}'.format(url[2:]),headers=headers)
    r.encoding = ('gb2312')
    se = etree.HTML(r.text)
    title = se.xpath('//div[@class="top-title"]/h2/text()')
    top = se.xpath('//td[@class="first"]/span/text()')
    name = se.xpath('//td[@class="keyword"]/a[@class="list-title"]/text()')
    score = se.xpath('//td[@class="last"]/span/text()')
    href = se.xpath('//td[@class="tc"]/a/@href')
    jianjie = href[0::3]
    tieba = href[1::3]
    pic = href[2::3]
    print(title)





