import requests
from lxml import etree
for i in range(1,20):
    r=requests.get('https://www.amazon.cn/s/page={}&keywords=手机'.format(i)).text
    se = etree.HTML(r)
    href = se.xpath('//a[@class="a-link-normal s-access-detail-page  s-color-twister-title-link a-text-normal"]/@href')
    for i in href:
        print(i)
        html = requests.get(i).text
        sel = etree.HTML(html)
        title = sel.xpath('//span[@class="a-size-large"]/text()')
        price = sel.xpath('//span[@class="a-size-medium a-color-price"]/text()')
        comment = sel.xpath('//span[@class="a-size-base"]/text()')
        print(title[0].replace('\n ',''),price[0].replace('\n ',''),comment[0].replace('\n ',''))


