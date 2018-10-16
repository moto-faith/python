import requests
from lxml import etree
import re
import json


headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}


for i in range(1,500):
    r= requests.get('http://s.manmanbuy.com/Default.aspx?PageID={}&key=apple'.format(i),headers = headers).text
    se = etree.HTML(r)
    title = re.findall('<font class="spnamehighword">.*?</font>(.*?)</a>',r,re.S)
    price = se.xpath('//span[@class="listpricespan"]/text()')
    shop = se.xpath('//p[@class="m"]/a/text()')
    comment = se.xpath('//div[@class="comment"]/a/text()')
    isZiying = se.xpath('//p[@class="AreaZY"]/text()')
    url = se.xpath('//div[@class="pic"]/a/@href')
    print(title)
    print(price)
    print(shop)
    print(comment)
    print(isZiying)
    print(url)




