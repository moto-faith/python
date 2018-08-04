
import requests
import re
import xlwt

def get_url():
    for i in range(29):
        url = 'http://s.yingjiesheng.com/search.php?word=python%E5%AE%9E%E4%B9%A0&area=1056&sort=score&start={}'.format(i*10)
        get_text(url)

def get_text(url):
    global total_href,total_title,total_time,total_text
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'}
    r=requests.get(url,headers=header).text
    href = re.findall('<h3 class="title"><a href="(.*?)" target="_blank">',r,re.S)
    title = re.findall('<h3 class="title"><a href=".*?" target="_blank">(.*?)</a></h3>',r,re.S)
    time = re.findall('<span class="r date" title="发布日期">(.*?)</span>',r,re.S)
    text = re.findall('职位简介：(.*?)<br />\r\n',r,re.S)

    for i in range(len(title)):
        tit=str(title[i]).replace('</em>','').replace('<em>','')
        title[i]=tit

    for j in range(len(text)):
        tex=str(text[j]).replace('</em>','').replace('<em>','')
        text[j]=tex
    total_href+=href
    total_title+=title
    total_time+=time
    total_text+=text



global total_href,total_title,total_time,total_text

total_href=[]
total_title=[]
total_time=[]
total_text=[]

def w2xls(href,title,time,text):
    global nums
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet("招聘信息")
    form = ["编号","网址","公司名","时间","详细内容"]
    for m in range(len(form)):
        worksheet.write(0,m,form[m])
    for k in range(len(href)):
        worksheet.write(k+1,0,k+1)
        worksheet.write(k+1,1,href[k])
        worksheet.write(k+1,2,title[k])
        worksheet.write(k+1,3,time[k])
        worksheet.write(k+1,4,text[k])


    workbook.save("test4.xls")
    return len(href)






if __name__ == '__main__':
    get_url()
    nums = w2xls(total_href,total_title,total_time,total_text)
    print("已经保存了{}条数据到 test4.xls中".format(nums))