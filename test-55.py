import re
import requests
import json

cookies = {
    'Cookie':'登录后产生的cookie复制到这里'
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

r = requests.get('https://tieba.baidu.com/index.html',cookies = cookies,headers = headers).text
kws = re.findall('"forum_name":"(.*?)",',r)

for kw in set(kws):
    word = "u'"+kw+"'"
    title = eval(word)
    r1 = requests.get('http://tieba.baidu.com/f?kw={}'.format(title),cookies=cookies,headers=headers).text
    tbs = re.findall('\'tbs\': "(.*?)"',r1)[0]
    # print(tbs) # 获得tbs

    data = {
        'ie': 'utf-8',
        'kw': title,
        'tbs': tbs,
    }

    r2 = requests.post('https://tieba.baidu.com/sign/add',data=data,cookies=cookies,headers=headers).text
    try:
        result = json.loads(r2)["data"]["errmsg"]
        print(title,result)
    except:
        print(title,'已经签过')
print('所有贴吧已签到完成')






