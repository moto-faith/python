import requests
import json
import re
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from pymongo import *

# 忽略警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

# 连接
client = MongoClient(host='localhost', port=27017)
# 选择库
db = client.bili
# 选择集合
test_set = db.userinfo


headers = {
    'Accept':'application/json, text/plain, */*',
    'Accept-Language':'zh-CN,en-US;q=0.8',
    'User-Agent':'Mozilla/5.0 (Linux; Android 7.1.1; ONEPLUS A5000 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.0.0 Mobile Safari/537.36',
    'X-Requested-With':'com.android.browser',
}
def detail(mid):
    r = requests.get('https://api.bilibili.com/x/space/app/index?mid={}'.format(mid),headers=headers,verify = False).text
    info = json.loads(r)["data"]["info"]
    test_set.insert(
        {"mid": info["mid"], 'name': info["name"], 'sex': info["sex"], 'face': info["face"], "sign": info["sign"],
         "level": info["level"], "following": info["following"], "follower": info["follower"]})
    print(info["mid"], info["name"], info["sex"], info["face"], info["sign"], info["level"], info["following"],
          info["follower"])




# https://api.bilibili.com/x/space/app/index?mid=16656459&platform=android
def main(mid):
    for i in range(1,50):
        r= requests.get('https://api.bilibili.com/x/relation/followings?vmid={}&order=desc&pn={}'.format(mid,i),headers = headers,verify=False).text
        data = json.loads(r)['data']

        if len(data['list'])==50:
            for i in data['list']:
                    detail(mid=i['mid'])
        else:
            for i in data['list']:
                detail(mid=i['mid'])
            print(i['mid'],'的关注者爬取完成')
            break

main(21)


# mid name sex face sign level following follower