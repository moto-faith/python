import requests
from lxml import etree
import json
import execjs

word = 'like a hot knife through butter'

with open('google.js')as f:
    js = f.read()

do = execjs.compile(js).call('TL',word)

r = requests.get('https://translate.google.cn/translate_a/single?client=t&sl=auto&tl=zh-CN&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&source=bh&ssel=0&tsel=0&kc=5&tk={}&q={}'.format(do,word)).text
r = json.loads(r)
print(r[0][0][0])
