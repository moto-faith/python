import re
import time
import xlwt
from selenium import webdriver
username = '123456'#学号
password = '123456'#密码
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://dean.cidp.edu.cn/')
driver.find_element_by_class_name('login').send_keys(username)
driver.find_element_by_class_name('password').send_keys(password)
driver.find_element_by_xpath('//*[@id="ulLogin"]/li[3]/button').click()
time.sleep(1)
js = "window.open('http://jwauth.cidp.edu.cn//NoMasterJumpPage.aspx?URL=JWGL')"
driver.execute_script(js)
handles = driver.window_handles
driver.switch_to.window(handles[1])
js = "window.open('http://jw.cidp.edu.cn/Teacher/MarkManagement/StudentAverageMarkSearchFZ.aspx')"
driver.execute_script(js)
handles = driver.window_handles
driver.switch_to.window(handles[2])
time.sleep(10)
a=driver.page_source
#一学年
#课程名
name1=re.findall('<td style="width:15%">(.*?)</td>',a,re.S)
 #分数
score1=re.findall('<td style="width:15%">.*?</td><td style="width:5%">.*?</td><td style="width:5%">.*?</td><td style="width:5%">.*?</td><td style="width:5%">(.*?)</td><td style="width:5%">.*?</td><td style="width:5%;display:none;">',a,re.S)
 #二学年
driver.find_element_by_id('year1').click()
b=driver.page_source
#课程名
name2=re.findall('<td style="width:15%">(.*?)</td>',b,re.S)
 #分数
score2=re.findall('<td style="width:15%">.*?</td><td style="width:5%">.*?</td><td style="width:5%">.*?</td><td style="width:5%">.*?</td><td style="width:5%">(.*?)</td><td style="width:5%">.*?</td><td style="width:5%;display:none;">',b,re.S)
 #三学年
driver.find_element_by_id('year2').click()
c=driver.page_source
#课程名
name3=re.findall('<td style="width:15%">(.*?)</td>',c,re.S)
 #分数
score3=re.findall('<td style="width:15%">.*?</td><td style="width:5%">.*?</td><td style="width:5%">.*?</td><td style="width:5%">.*?</td><td style="width:5%">(.*?)</td><td style="width:5%">.*?</td><td style="width:5%;display:none;">',c,re.S)
name = name1+name2+name3
score = score1+score2+score3
f=xlwt.Workbook(encoding='utf-8')
sheet = f.add_sheet('成绩')
title = ['学科','成绩']
for i in range(len(title)):
    sheet.write(0,i,title[i])
 for j in range(len(name)):
    sheet.write(j+1,0,name[j])
    sheet.write(j+1,1,score[j])
 f.save('期末成绩.xls')
