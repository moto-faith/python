import re
import requests
import json
data = {
    'image':open('1.png','rb')
}
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
r = requests.post('https://graph.baidu.com/upload?tn=pc&from=pc&image_source=PC_UPLOAD_IMAGE_MOVE&range={%22page_from%22:%20%22shituIndex%22}&extUiData%5bisLogoShow%5d=1',files=data,headers = headers).text
url = json.loads(r)["data"]["url"]
r1 = requests.get(url,headers = headers).text
name = re.findall('"subTitle":"(.*?)",',r1)[0]
a = "u'"+name+"'"
print(eval(a))
