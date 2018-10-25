import requests
import re
from lxml import etree
import urllib.request
from pymongo import *

# 连接
client = MongoClient(host='localhost', port=27017)
# 选择库
kuwo = client.kuwo
# 选择集合
song = kuwo.song

songid = '3565454'

r = requests.get(
    'http://comment.kuwo.cn/com.s?type=get_comment&uid=0&prod=newWeb&digest=15&sid={}&page=1&rows=20&f=web&jpcallback=getCommentListFn'.format(songid))
totalPage = int(re.findall('"totalPage":"(.*?)"', r.text)[0])
for page in range(1,totalPage+1):
    r = requests.get(
        'http://comment.kuwo.cn/com.s?type=get_comment&uid=0&prod=newWeb&digest=15&sid={}&page={}&rows=20&f=web&jpcallback=getCommentListFn'.format(songid,page))
    text = urllib.request.unquote(r.text)
    ids = re.findall('"id":"(.*?)"', text)
    u_pics = re.findall('"u_pic":"(.*?)"', text)
    u_names = re.findall('"u_name":"(.*?)"', text)
    times = re.findall('"time":"(.*?)"', text)
    like_nums = re.findall('"like_num":"(.*?)"', text)
    msgs = re.findall('"msg":"(.*?)"', text)

    for id,u_pic,u_name,time,like_num,msg in zip(ids,u_pics,u_names,times,like_nums,msgs):
        song.insert({'id':id,'u_pic':u_pic,'u_name':u_name,'time':time,'like_num':like_num,'msg':msg})
    print('第{}页完成'.format(page))
