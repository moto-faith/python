import requests
from urllib import request
import re
import json
import pytesseract
from PIL import Image
from lxml import etree

cookie = {
    'Cookie':'登录产生的cookie'
}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
    'Host':'jy.cidp.edu.cn',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Connection':'keep-alive',
    'Referer':'http://jy.cidp.edu.cn/student/myarchives.php',
}

r=requests.get('http://jy.cidp.edu.cn/student/archives_scan.php',cookies = cookie,headers=headers)
r.encoding = ('gb2312')
yuan = re.findall('所在院系</td>.*?>(.*?)</td>',r.text,re.S)[0]
ban = re.findall('所在班级：</td>.*?>(.*?)</td>',r.text,re.S)[0]
id = re.findall('学号：</td>.*?>(.*?)</td>',r.text,re.S)[0]
shenFenzheng = re.findall('身份证号：</td>.*?>(.*?)</td>',r.text,re.S)[0]
name = re.findall('姓名：</td>.*?>(.*?)</td>',r.text,re.S)[0]
gender = re.findall('性别：</td>.*?>(.*?)</td>',r.text,re.S)[0]
birth = re.findall('出生日期：</td>.*?>(.*?)</td>',r.text,re.S)[0]
zhuanye = re.findall('专业：</td>.*?>(.*?)</td>',r.text,re.S)[0]
intime = re.findall('入学时间：</td>.*?>(.*?)</td>',r.text,re.S)[0]
outtime = re.findall('毕业时间：</td>.*?>(.*?)</td>',r.text,re.S)[0]
tel = re.findall('移动电话：</td>.*?>(.*?)</td>',r.text,re.S)[0]
mail = re.findall('电子邮箱：</td>.*?>(.*?)</td>',r.text,re.S)[0]
qq = re.findall('QQ：</td>.*?>(.*?)</td>',r.text,re.S)[0]
address = re.findall('家庭地址：</td>.*?>(.*?)</td>',r.text,re.S)[0]
print(yuan)
print(ban)
print(id)
print(shenFenzheng)
print(name)
print(gender)
print(birth)
print(zhuanye)
print(intime)
print(outtime)
print(tel)
print(mail)
print(qq)
print(address)


