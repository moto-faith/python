import requests
import json
import execjs
import urllib.request
from pymongo import *

# 连接
client = MongoClient(host='localhost', port=27017)
# 选择库
yanyuan = client.yanyuan
# 选择集合
comment = yanyuan.comment

songid = '32507038'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Content-Length': '472',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Cookie': '_iuqxldmzr_=32; _ntes_nnid=e627cf9a74617a73569fd5a0b24c2cd1,1532830743304; _ntes_nuid=e627cf9a74617a73569fd5a0b24c2cd1; WM_TID=l91D35jYztZzK3dRLDdMeY7k6li9BqrM; __f_=1532860604840; vjuids=-203e844d2.1656b1ffe57.0.199f534267f6f; vjlast=1535100584.1535100584.30; usertrack=ezq0pFuTZaoad8JnN3ibAg==; _ga=GA1.2.1692919701.1536386476; P_INFO=15510133572|1535680523|2|study|00&99|null&null&null#heb&130200#10#0#0|&0|null|15510133572; vinfo_n_f_l_n3=bc06b141e78ae913.1.2.1534495094601.1535100610100.1540262234696; JSESSIONID-WYYY=2OV7f9fit7aqpouq8wnmkF6N5Ai%2FOlffB9%2F000ufOjgEasEED9jW4dcEq6HvdhfXoCY%2BWo7iP%2FdTksVzwDr8Mu1lMuNq2q6GBHu%5Cl%2Fu%2FoO097Fj2VjQaNxMeXUOfQSB8nN5G5g8AggDcuyfoEgCs2n1E8jdhQ7dVtZoO9E%5CxVeEiy4eb%3A1540341542877; __utma=94650624.1051731555.1532830744.1540259463.1540339743.47; __utmc=94650624; __utmz=94650624.1540339743.47.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; WM_NI=h4WkZTJLPDhmX5NY8ksMEJzYVCqxKZGHuRUXI36zgquF6Wno9e4Zc4JBA9z%2BPhbvC4DG6iOCTS5WDheAVeDBN0EswCK4%2F%2FT6wtzhty16G9ZbqV0%2BE1AhvnF1AQBYnKRoWWs%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeaee97dad88828ad37c8c968fa6d85a928a8a85f36e8ab5aaacc76590f1feaef72af0fea7c3b92aacec998cd9608a94a0a5eb679ceb82babb61b1938babf953969dbf99ca528598bbb3d8548bedfa9be67bb79afab8ed65fbbbfcbbe2408a9e8fdaf92194b8ae97c2408899fa8ace49988dfbb8c764a79f9a86c74a8ef08b94f64989ece1d0d73eb5acb689f773f3ea89dad96ab38a00ccc83b83b8ba8fc53b838f8ebaed4192b199b8f237e2a3; __utmb=94650624.6.10.1540339743'
}
for i in range(0,10):
    offset = i*20
    dict1={
        'rid':'R_SO_4_{}'.format(songid),
        'limit':'20',
        'offset':'{}'.format(offset),
        'total':'true'
    }
    d = json.dumps(dict1)
    e = '010001'
    f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    g = '0CoJUm6Qyw8W8jud'

    with open('WYmusic/yunmusic.js')as file:
        js = file.read()

    dict = execjs.compile(js).call('d', d, e, f, g)
    data = {
                    'params': dict['encText'],
                    'encSecKey': dict['encSecKey']
                }
    r=requests.post('https://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token='.format(songid),headers=headers,data=data).text
    comments = json.loads(r)['comments']
    contents = [comment['content'] for comment in comments]
    times = [comment['time'] for comment in comments]
    likedCounts=[comment['likedCount'] for comment in comments]
    avatarUrls=[comment['user']['avatarUrl'] for comment in comments]
    nicknames = [comment['user']['nickname'] for comment in comments]
    userIds = [comment['user']['userId'] for comment in comments]
    for content,time,likedCount,avatarUrl,nickname,userId in zip(contents,times,likedCounts,avatarUrls,nicknames,userIds):
        comment.insert({'content':content,'time':time,'likedCount':likedCount,'avatarUrl':avatarUrl,'nickname':nickname,'userId':userId})
    print('已爬取',i,'页')