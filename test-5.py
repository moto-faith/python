import requests
import xlwt
from urllib import request
import os

def select(nums):
    os.mkdir('./pic')
    chose={}
    chose['age']=input("对方年龄:(选填)")
    if chose['age']=='':
        chose['age'] = ''
    elif 21<=int(chose['age']) and int(chose['age'])<=30:
        chose['age']='startage=21&endage=30&'
    elif 31<=int(chose['age']) and int(chose['age'])<=40:
        chose['age']='startage=31&endage=40&'
    elif 41<=int(chose['age']) and int(chose['age'])<=50:
        chose['age']='startage=41&endage=50&'
    elif 51<=int(chose['age']) and int(chose['age'])<=60:
        chose['age']='startage=51&endage=60&'
    elif 61<=int(chose['age']):
        chose['age']='startage=61&endage=99&'
    else:
        print('您输入的年龄错误,已默认不限年龄')
        chose['age'] = ''
    #------------------------------------------------------#
    chose['gender']=input('对方性别:(必填)')
    if chose['gender']=='男':
        chose['gender'] = 'gender=1&'
    elif chose['gender']=='女':
        chose['gender'] = 'gender=2&'
    else:
        print('您输入的性别错误,已默认对方为女性')
        chose['gender'] = 'gender=2&'
    # ------------------------------------------------------#
    chose['city']=input('对方城市:(选填)')
    if chose['city']=='':
        chose['city']='cityid=0&'
    elif chose['city']=='北京':
        chose['city'] ='cityid=52&'
    elif chose['city'] == '深圳':
        chose['city'] ='cityid=77&'
    elif chose['city'] == '广州':
        chose['city'] ='cityid=76&'
    elif chose['city'] == '福州':
        chose['city'] ='cityid=53&'
    elif chose['city'] == '厦门':
        chose['city'] ='cityid=60&'
    elif chose['city'] == '杭州':
        chose['city'] ='cityid=383&'
    elif chose['city'] == '青岛':
        chose['city'] ='cityid=284&'
    elif chose['city'] == '长沙':
        chose['city'] ='cityid=197&'
    elif chose['city'] == '济南':
        chose['city'] ='cityid=283&'
    elif chose['city'] == '南京':
        chose['city'] ='cityid=220&'
    elif chose['city'] == '香港':
        chose['city'] ='cityid=395&'
    elif chose['city'] == '上海':
        chose['city'] ='cityid=321&'
    elif chose['city'] == '成都':
        chose['city'] ='cityid=322&'
    elif chose['city'] == '武汉':
        chose['city'] ='cityid=180&'
    elif chose['city'] == '苏州':
        chose['city'] ='cityid=221&'
    else:
        chose['city'] = 'cityid=0&'
        print('您输入的城市暂时没有,已默认为不限城市')
    # ------------------------------------------------------#
    chose['height']=input('对方身高(选填)')
    if chose['height']=='':
        chose['height']=''
    elif int(chose['height'])<=150:
        chose['height']='startheight=0&endheight=150&'
    elif 151<=int(chose['height']) and int(chose['height'])<=160:
        chose['height'] = 'startheight=151&endheight=160&'
    elif 161<=int(chose['height']) and int(chose['height'])<=170:
        chose['height'] = 'startheight=161&endheight=170&'
    elif 171<=int(chose['height']) and int(chose['height'])<=180:
        chose['height'] = 'startheight=171&endheight=180&'
    elif 181<=int(chose['height']) and int(chose['height'])<=190:
        chose['height'] = 'startheight=181&endheight=190&'
    elif 191<=int(chose['height']):
        chose['height'] = 'startheight=190&endheight=250&'
    else:
        chose['height']=''
        print('您输入的身高错误,已默认不限身高')

    # ------------------------------------------------------#
    chose['marry']=input('对方婚姻状况(必填)')
    if chose['marry']=='未婚':
        chose['marry']='marry=1&'
    elif chose['marry']=='离异':
        chose['marry'] = 'marry=3&'
    elif chose['marry']=='丧偶':
        chose['marry'] = 'marry=4&'
    else:
        chose['marry']='marry=1&'
        print('您输入的婚姻状况错误,已默认未婚')
    # ------------------------------------------------------#

    chose['education']=input('对方教育水平(选填)')

    if chose['education']=='':
        chose['education'] = ''
    elif chose['education']=='初中':
        chose['education'] = 'education=10&'
    elif chose['education']=='高中':
        chose['education'] = 'education=20&'
    elif chose['education']=='中专':
        chose['education'] = 'education=25&'
    elif chose['education']=='大专':
        chose['education'] = 'education=30&'
    elif chose['education']=='本科':
        chose['education'] = 'education=40&'
    elif chose['education']=='硕士':
        chose['education'] = 'education=50&'
    elif chose['education']=='博士':
        chose['education'] = 'education=60&'
    elif chose['education']=='院士':
        chose['education'] = 'education=70&'
    else:
        chose['education'] = ''
        print('您输入的教育水平错误,已默认为不限')

    # ------------------------------------------------------#

    chose['salary']=input('对方薪资水平(选填)')
    if chose['salary']=='':
        chose['salary'] =''
    elif int(chose['salary'])<5000:
        chose['salary']='salary=2&'
    elif 5000<=int(chose['salary']) and int(chose['salary'])<10000:
        chose['salary']='salary=3&'
    elif 10000<=int(chose['salary'])and int(chose['salary'])<20000:
        chose['salary']='salary=4&'
    elif 20000<=int(chose['salary']):
        chose['salary']='salary=5&'
    else:
        chose['salary'] = ''
        print('您输入的金额错误,已默认为不限')
    print('请稍等,正在获取信息...')

    url = 'http://www.lovewzly.com/api/user/pc/list/search?'+chose['age']+chose['gender']+chose['city']+chose['height']+chose['marry']+chose['education']+chose['salary']+'page='
    get_text(url,nums)
def get_text(url,nums):
    userid=[]
    province=[]
    city=[]
    height=[]
    education=[]
    username=[]
    monolog=[]
    birthdayyear=[]
    avatar=[]
    gender=[]
    num=int(nums/20)+1
    for i in range(1,num):
        n_url = url+str(i)
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'}
        r = requests.get(n_url,headers=headers).json()
        for k in range(20):
            userid.append(r['data']['list'][k]['userid'])
            province.append( r['data']['list'][k]['province'])
            city.append(r['data']['list'][k]['city'])
            height.append(r['data']['list'][k]['height'])
            education.append(r['data']['list'][k]['education'])
            username.append(r['data']['list'][k]['username'])
            monolog.append(r['data']['list'][k]['monolog'])
            birthdayyear.append(r['data']['list'][k]['birthdayyear'])
            avatar.append(r['data']['list'][k]['avatar'])
            gender.append("女" if r['data']['list'][k]['gender']=='2' else "男")



    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet("个人信息")
    title = ['编号','昵称','性别','生年','身高','教育','省份','城市','留言']
    for m in range(len(title)):
        worksheet.write(0,m,title[m])
    for n in range(len(userid)):
        worksheet.write(n+1,0,userid[n])
        worksheet.write(n + 1, 1, username[n])
        worksheet.write(n + 1, 2, gender[n])
        worksheet.write(n + 1, 3, birthdayyear[n])
        worksheet.write(n + 1, 4, height[n])
        worksheet.write(n + 1, 5, education[n])
        worksheet.write(n + 1, 6, province[n])
        worksheet.write(n + 1, 7, city[n])
        worksheet.write(n + 1, 8, monolog[n])
        request.urlretrieve(avatar[n],'./pic/{}.png'.format(userid[n]))

    workbook.save('test5.xls')

if __name__ == '__main__':
    nums=int(input("您想获取多少人的信息:"))
    select(nums)
    print("您已获取{}人的信息,数据保存为test5.xls,图片保存到pic文件夹下".format(nums))









