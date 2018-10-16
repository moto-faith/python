import requests
import re
import json
from lxml import etree
import time
e=requests.get('http://data.cnki.net/Yearbook/Single/N2017100312').text
ids = re.findall('<a href="/Yearbook/Single/(.*?)"',e)

for id in ids:
    for i in range(1,41):
        time.sleep(1)
        data = {
        'ybcode':id,
        'entrycode':'',
        'page':i,
        'pagerow':'20',
        }

        r=requests.post('http://data.cnki.net/Yearbook/PartialGetCatalogResult',data=data).text
        se = etree.HTML(r)
        down = se.xpath('//*[@id="ResultList_jy"]/table/tr/td[3]/a[2]/@href')
        index = se.xpath('//a[@class="model_a"]/span/text()')
        print(down)
        print(index)