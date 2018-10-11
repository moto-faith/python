import requests
import random
import json

token = '登录公众号后网址里的token'
word = '想搜索的关键词'
cook = '填上登录产生的cookie'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Connection': 'keep-alive',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
}
cookie = {
    'Cookie': cook
}

# 搜索微信公众号的接口地址
search_url = 'https://mp.weixin.qq.com/cgi-bin/searchbiz?'
# 搜索微信公众号接口需要传入的参数，有三个变量：微信公众号token、随机数random、搜索的微信公众号名字
for i in range(0,51,5):# 这里循环的是公众号数量
    query_id = {
        'action': 'search_biz',
        'token': token,
        'lang': 'zh_CN',
        'f': 'json',
        'ajax': '1',
        'random': random.random(),
        'query': word,
        'begin': i,
        'count': '5'
    }
    # 打开搜索微信公众号接口地址，需要传入相关参数信息如：cookies、params、headers
    search_response = requests.get(search_url, cookies=cookie, headers=header, params=query_id)
    # 取搜索结果中的第一个公众号
    lists = search_response.json().get('list')
    # 获取这个公众号的fakeid，后面爬取公众号文章需要此字段
    fakeids = [list.get('fakeid')for list in lists]
    for fakeid in fakeids:# 遍历每个公众号
        for k in range(0,51,5):# 遍历该公众号内所有文章
            url = 'https://mp.weixin.qq.com/cgi-bin/appmsg?token={}&lang=zh_CN&f=json&ajax=1&random=0.578791056424645&action=list_ex&begin={}&count=5&query=&fakeid={}&type=9'.format(token,k,fakeid)
            r=requests.get(url=url,headers=header,cookies = cookie).text
            list = json.loads(r)["app_msg_list"]
            for i in list:
                print(i["title"])
                print(i["link"])

