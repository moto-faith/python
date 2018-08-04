# coding:utf-8
import requests
import json
from lxml import etree


def search_info(keyword):

    results_list = []
    # 这里可以研究得出关键是后面变化的关键词
    url = 'https://www.baidu.com/s?word={}'.format(keyword)

    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400'
    }

    response = requests.get(url,headers = headers)
    response.encoding = 'utf-8'
    source = etree.HTML(response.text)
    results = source.xpath('//*[@id]/@data-tools')
    for r in results:
        try:
            # 这里需要对 xpath取取的结果进行转码：<type 'lxml.etree._ElementUnicodeResult'> 转成str
            # 然后再把字符串转换成json，再取值
            str = json.loads(r.encode('utf-8'))
            results_list.append(str)

        except Exception as e:
            continue
    return results_list
