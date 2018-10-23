import json
import execjs
import requests
import urllib.request

keyWord = '绅士'# 歌曲名称

list = {'s': keyWord, 'limit': '20', 'type': '1', 'csrf_token': '046a07c4cb59ef4c82571fe260e3b36b'}# limit为歌曲数量
d = json.dumps(list)
e = '010001'
f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
g = '0CoJUm6Qyw8W8jud'

with open('yunmusic.js')as file:
    js = file.read()

dict = execjs.compile(js).call('d', d, e, f, g)
data = {
                'params': dict['encText'],
                'encSecKey': dict['encSecKey']
            }
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Host': 'music.163.com',
    'Origin': 'https://music.163.com',
    'Referer': 'https://music.163.com/search/',
    'Accept': '*/*',
    'Cookie': '_iuqxldmzr_=32; _ntes_nnid=e627cf9a74617a73569fd5a0b24c2cd1,1532830743304; _ntes_nuid=e627cf9a74617a73569fd5a0b24c2cd1; WM_TID=l91D35jYztZzK3dRLDdMeY7k6li9BqrM; __f_=1532860604840; vjuids=-203e844d2.1656b1ffe57.0.199f534267f6f; vjlast=1535100584.1535100584.30; vinfo_n_f_l_n3=bc06b141e78ae913.1.1.1534495094601.1534495138339.1535100610100; P_INFO=15510133572|1535680523|1|study|00&99|null&null&null#heb&130200#10#0#0|&0|null|15510133572; usertrack=ezq0pFuTZaoad8JnN3ibAg==; _ga=GA1.2.1692919701.1536386476; JSESSIONID-WYYY=clu4FIV4q6GXPfrg4pcPfXA75oal1nbOgba7r1IqTQzPaQvC1NobEIkUhtzwcJipIhZNkH14EP0R7XkRnIDWrd7mrKZwBSCy6hhv%2F%2FysVKDEf08YGVBWyfcTY%2BEwZWg0Ayj%2B36fifWhumQWn7t7ZC4gvj%5CoFGADz%2BiuzTO%2BHqycxA4Hy%3A1540261263106; __utma=94650624.1051731555.1532830744.1540180180.1540259463.46; __utmc=94650624; __utmz=94650624.1540259463.46.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; WM_NI=%2BBg%2Fm8EhIOQRR6uL%2Fc13GV8eAONYAseD6H41MWNDw%2BaEeG9AXdfH2gGWFzUNsLf0inI0L2DpKIHjEv6SFpsOezxk%2Fp7Ez1P5xIUOCTqJvt%2BjEMx4d6BCV4HEQTgoPJFwUEs%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee89ec608bb7beaedb7ef18a8fb6c44f868f9baebb459b91fbd2f57df28f9eb7d92af0fea7c3b92ae99ea9d0f03487b887b0d45a92eabbadae69f3ed89b7bb6f839182bac479a79cfaa9b73b8f8982a5f621a39baba8bc4b9cbcaaa9b16d85898a9bd846b194aad1ec668bf084d3c77c8997888bc87ef68d8a91f245a7a6b88cae7cf59bb6d2d33fbc979bb0c260b396ba95aa628793b8d5e73e829d9ad5cb4f938ca990d34286a99ba6f237e2a3; __utmb=94650624.8.10.1540259463'
}
response = requests.post('https://music.163.com/weapi/cloudsearch/get/web?csrf_token=',headers=headers,data=data).text
songs = json.loads(response)["result"]["songs"]
name = [song['name'] for song in songs]
singer=[]
for song in songs:
    singer.append(song['ar'][0]['name'])
id = [song['id'] for song in songs]
for i in range(0,len(id)):
    urllib.request.urlretrieve('http://music.163.com/song/media/outer/url?id={}.mp3'.format(id[i]),'music/{}-{}.mp3'.format(name[i],singer[i]))
    print(name[i],singer[i],'is download')
