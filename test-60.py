import requests
import json
import re
from lxml import etree
for bigPage in range(0,51):
    for small in range(0,4):
        r=requests.get('https://search.suning.com/emall/searchV1Product.do?keyword=手机&ci=0&pg=01&cp={}&il=0&st=0&iy=0&n=1&sesab=ACAABAAB&id=IDENTIFYING&cc=316&paging={}&sub=1'.format(bigPage,small)).text
        se = etree.HTML(r)
        urls = se.xpath('//div[@class="title-selling-point"]/a/@href')
        for url in urls:
            id = re.findall('/product.suning.com/.*?/(.*?).html',url)
            item_url = 'https://tuijian.suning.com/recommend-portal/dyBase.jsonp?parameter='+(18-len(id[0]))*'0'+id[0]+'&sceneIds=1-1&count=20&callback=Recommend.getRecomData'
            items = requests.get(item_url).text
            names = re.findall('"sugGoodsName":"(.*?)"',items)
            prices = re.findall('"price":"(.*?)"',items)
            reprices = re.findall('"refPrice":"(.*?)"', items)
            for name,price,reprice in zip(names,prices,reprices):
                print(name,price,reprice)

# https://tuijian.suning.com/recommend-portal/dyBase.jsonp?parameter=000000000612988189&sceneIds=1-1&count=20&callback=Recommend.getRecomData
# https://tuijian.suning.com/recommend-portal/dyBase.jsonp?parameter=000000010492085586&sceneIds=1-1&count=20&callback=Recommend.getRecomData
