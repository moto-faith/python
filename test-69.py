import requests
import urllib.request
import json

word = '演员'
r = requests.get(
    'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w={}'.format(
        word))  # pn为页数，n为每页的数量如果需要可以遍历多页
songlist = json.loads(r.text.strip('callback()[]'))['data']['song']['list']
songmids = []
srcs = []
songnames = []
singers = []
for song in songlist:
    try:
        songmids.append(song['songmid'])
        songnames.append(song['songname'])
        name = [names['name'] for names in song['singer']]  # 多人合唱时把名字全部提出
        singers.append(name)
    except:
        print('该歌曲不存在')

for n in songmids:
    res2 = requests.get(
        'https://c.y.qq.com/base/fcgi-bin/fcg_music_express_mobile3.fcg?&jsonpCallback=MusicJsonCallback&cid=205361747&songmid=' + n + '&filename=C400' + n + '.m4a&guid=6612300644')
    jm2 = json.loads(res2.text)
    vkey = jm2['data']['items'][0]['vkey']
    srcs.append('http://dl.stream.qqmusic.qq.com/C400' + n + '.m4a?vkey=' + vkey + '&guid=6612300644&uin=0&fromtag=66')

x = len(srcs)
for m in range(0, x):
    try:
        urllib.request.urlretrieve(srcs[m], 'music/{} - {}.m4a'.format(songnames[m], singers[m]))

    except:
        print('下载错误')

    else:
        print('music/{} - {}.m4a'.format(songnames[m], singers[m]),'下载成功')


