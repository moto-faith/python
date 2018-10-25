import requests
import json
import re
from lxml import etree
from pymongo import *
import urllib.request


# 连接
client = MongoClient(host='localhost', port=27017)
# 选择库
kugou = client.kugou
# 选择集合
song = kugou.song


# print(hash)
for id in range(1,1000):
    response = requests.get('http://www.kugou.com/yy/singer/home/{}.html'.format(id)).text
    se = etree.HTML(response)
    values = se.xpath('//input[@checked="checked"]/@value')
    hashs = [value.split('|')[1] for value in values]
    for hash in hashs:
        r = requests.get('http://wwwapi.kugou.com/yy/index.php?r=play/getdata&hash={}'.format(hash))
        s = r.text.encode('utf-8').decode('unicode_escape')
        play_url = re.findall('"play_url":"(.*?)"', s)[0].replace('\\', '')
        bitrate = re.findall('"bitrate":(.*?)}', s)[0]
        audio_name = re.findall('"audio_name":"(.*?)"', s)[0]
        author_name = re.findall('"author_name":"(.*?)"', s)[0]
        song_name = re.findall('"song_name":"(.*?)"', s)[0]
        lyrics = re.findall('"lyrics":"(.*?)",', s, re.S)[0]
        try:
            song.insert({'play_url': play_url, 'bitrate': bitrate, 'audio_name': audio_name, 'author_name': author_name,
                         'song_name': song_name, 'lyrics': lyrics})
            urllib.request.urlretrieve(play_url,'music/{}-{}.mp3'.format(song_name,author_name))# 下载到本地
            print(audio_name,'已下载完成')
        except:
            print(hash,'下载错误')