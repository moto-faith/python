import requests
import re
from lxml import etree
import urllib.request

word = '演员'

response = requests.get('http://sou.kuwo.cn/ws/NSearch?key={}&type=music&pn=1'.format(word)).text
se = etree.HTML(response)
number = int(re.findall('pn=(.*)',se.xpath('//div[@class="page"]/a/@href')[-1])[0])
print('一共有',number,'页')
for page in range(1,number+1):
    response = requests.get('http://sou.kuwo.cn/ws/NSearch?key={}&type=music&pn={}'.format(word,page)).text
    se = etree.HTML(response)
    urls = se.xpath('//p[@class="m_name"]/a/@href')
    m_name = se.xpath('//p[@class="m_name"]/a/@title')
    a_name = se.xpath('//p[@class="a_name"]/a/@title')
    s_name = se.xpath('//p[@class="s_name"]/a/@title')
    ids = [url.split('/')[-2] for url in urls]
    for i in range(len(ids)):
        try:
            urllib.request.urlretrieve(
                'http://antiserver.kuwo.cn/anti.s?format=aac|mp3&rid=MUSIC_{}&type=convert_url&response=res'.format(ids[i]),
                'music/{}-{}.aac'.format(m_name[i],s_name[i]))
            print('{}-{}.aac'.format(m_name[i],s_name[i]),'下载成功')
        except:
            print(ids[i],'下载错误')
    print('第',page,'页下载完成')