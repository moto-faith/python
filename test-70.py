import requests
import urllib.request
import json
import re
from lxml import etree
import urllib.parse

word = '泡沫'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
}

response = requests.get('https://www.xiami.com/search/song?key={}'.format(word), headers=headers).text
se = etree.HTML(response)
ids = se.xpath('//input[@checked="checked"]/@value')
for songid in ids:
    try:
        r = requests.get('http://www.xiami.com/widget/xml-single/uid/0/sid/{}'.format(songid), headers=headers).text
        location = re.findall('<location><!\[CDATA\[(.*?)\]\]></location>', r, re.S)[0]
        name = re.findall('<song_name><!\[CDATA\[(.*?)\]\]></song_name>', r, re.S)[0]
        singer = re.findall('<artist_name><!\[CDATA\[(.*?)\]\]></artist_name>', r, re.S)[0]


        # 把location解为url地址
        num_loc = location.find('h')
        rows = int(location[0:num_loc])
        strlen = len(location) - num_loc
        cols = strlen / rows
        right_rows = strlen % rows
        new_s = location[num_loc:]
        output = ''
        for i in range(len(new_s)):
            x = i % rows
            y = i // rows
            p = 0
            if x <= right_rows:
                p = x * (cols + 1) + y
            else:
                p = right_rows * (cols + 1) + (x - right_rows) * cols + y

            output += new_s[int(p)]
        mp3 = urllib.parse.unquote(output).replace('^', '0')
        print(mp3)
        urllib.request.urlretrieve(mp3, 'music/{} - {}.mp3'.format(name, singer))
        print('{} - {}.mp3 下载完成'.format(name, singer))
    except:
        print(songid,'下载错误')
