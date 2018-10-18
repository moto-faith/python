import requests
import re
import json
from pymongo import *

# 连接
client = MongoClient(host='localhost', port=27017)
# 选择库
gaide = client.gaide
# 选择集合
paihang = gaide.product

headers = {
    # 'POST /guiderank-web/app/ranking/getRankingGlobalPage.do?token=jYmBfC8TCq0TUagEhZ0CbSt1du85bVMF&ver=android_3.3.0&role=1&model=ONEPLUS%20A5000&imei=99001062416537 HTTP/1.1',
    'Content-Type': 'application/json; charset=UTF-8',
    # 'Content-Length':'52',
    'Host': 'zone.guiderank-app.com',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/3.8.0',
}


def detail(categoryId):
    # 具体商品
    data = {
        "categoryId": categoryId,
        "rankingId": ""
    }
    req = json.dumps(data).encode('utf8')
    r = requests.post(
        'https://zone.guiderank-app.com/guiderank-web/app/ranking/getRankingGlobalPage.do?token=&ver=android_3.3.0&role=1&model=ONEPLUS%20A5000&imei=99001062416537',
        headers=headers, data=req).text
    classlei = json.loads(r)["data"]["globalPage"]['categoryName']  # 商品类别
    conducts = json.loads(r)["data"]["globalPage"]["rankingGlobals"]
    for conduct in conducts:
        brandName = conduct['brandName']  # 商品名称
        country = conduct['brand']['country']  # 所属国家
        comment = conduct['comment']  # 商品评价
        score = conduct['score']  # 商品分数
        seq = conduct['seq']  # 商品排名
        paihang.insert(
            {'tableName': classlei, 'brandName': brandName, 'country': country, 'comment': comment, 'score': score,
             'seq': seq})
    print(classlei,"的排行已完成")


def pin(rootCategoryId):
    # 品种id
    rootdata = {
        'rootCategoryId': rootCategoryId
    }
    rootdata = json.dumps(rootdata).encode('utf8')
    rooturl = 'https://zone.guiderank-app.com/guiderank-web/app/ranking/getRootCategoryById.do?token=&ver=android_3.3.0&role=1&model=ONEPLUS%20A5000&imei=99001062416537'
    rootResponse = requests.post(url=rooturl, data=rootdata, headers=headers).text
    categories = json.loads(rootResponse)['data']['rootCategory']['categories']
    for categorie in categories:
        categoryIds = [categoryId['categoryId'] for categoryId in categorie['categories']]
        for categoryId in categoryIds:
            detail(categoryId)


def rootclass():
    # 类的id
    # rootCategoryId = [14606182089902377708,14606181759902134838,14606181939902245329,14606182589902511282,14606181289901965889,14606181069901833410,14606180879901742083,14606180599901603729,14606180049901484947,14606180049901484946,15067481111500006673,14879256571502247876,14823046351581057672,14879242641500711705,14606180409901527039,14800587051514915035,14957723891559125047,14606179869901389369,14606178369901135650,14606182239902449726,14606178509901221118,14606123089900845018,14606181479902024599]
    r = requests.post(
        'https://zone.guiderank-app.com/guiderank-web/app/ranking/getFirstCategoryQueueByUser.do?token=&ver=android_3.3.0&role=1&model=ONEPLUS%20A5000&imei=99001062416537',
        headers=headers).text
    ids = json.loads(r)["data"]["categories"]
    classids = [categoryId['categoryId'] for categoryId in ids]  # 总共23个大类
    for classid in classids:
        pin(classid)


if __name__ == '__main__':
    rootclass()
