import requests
import re
from lxml import etree
import json
import urllib.parse


word = input('输入查询的地址：')
word = urllib.parse.quote(word.encode('gb2312'))
r=requests.get('http://opendata.baidu.com/post/s?wd={}'.format(word))
r.encoding = ('gbk')
se = etree.HTML(r.text)
number = se.xpath('/html/body/section/article[1]/table/tr[2]/td[1]/text()')[0]
address = se.xpath('/html/body/section/article[1]/table/tr[2]/td[2]/text()')[0]
detail_address = se.xpath('/html/body/section/article[1]/table/tr[2]/td[2]/em/text()')[0]
print(number,address,detail_address)

