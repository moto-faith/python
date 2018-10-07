import requests
import json
import execjs


word = input("输入需要翻译的英文：")

with open('baidu.js')as f:
    js = f.read()

do = execjs.compile(js).call('e',word)


data = {
    'from': 'en',# 输入的语言
    'to': 'jp', # 需要输出的语言
    'query': word, # 需要翻译的词或句子
    'transtype': 'realtime', # 常量
    'simple_means_flag': '3',# 常量
    'sign': do, # 由query生成的一个数字
    'token': '0f534e150e22f3a780e140e6411d808b',# 常量
}
headers = {
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Cookie': 'BIDUPSID=03A5054DE432A262CBAE5B7DDA1EE02E; PSTM=1532826405; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BAIDUID=03A5054DE432A262CBAE5B7DDA1EE02E:SL=0:NR=10:FG=1; MCITY=-%3A; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1538823259,1538823273,1538868603; to_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22jp%22%2C%22text%22%3A%22%u65E5%u8BED%22%7D%5D; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1538872647',
    'Host': 'fanyi.baidu.com',
    'Origin': 'https://fanyi.baidu.com',
    'Referer': 'https://fanyi.baidu.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
r = requests.post('https://fanyi.baidu.com/v2transapi', data=data, headers=headers).text
r = json.loads(r)

print('原文为：',word)
print('日语为：',r["trans_result"]["data"][0]['dst'])
