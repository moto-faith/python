import requests
import re
from lxml import etree
import csv
from multiprocessing import Pool


def html(web):
    r = requests.get(web).text
    s = etree.HTML(r)
    ifsale = re.findall('<span class="pull-left">(.*?)<span class="price">', r, re.S)
    ids = s.xpath('//*[@id="yw0"]/div[1]/ul/li/a/@href')
    id = re.findall('item_id=(\d+)&', str(ids), re.S)
    name = s.xpath('//*[@id="yw0"]/div[1]/ul/li/p[1]/a/span/text()')
    now_money = s.xpath('//*[@id="yw0"]/div[1]/ul/li/p[2]/span[1]/span/text()')
    now_moneys = []
    for now in now_money:
        now_moneys.append(now.replace("￥", ""))
    num = 0
    for i in id:
        hhtml = 'https://www.c5game.com/csgo/item/history/{}.html'.format(i)
        last = requests.get(hhtml).text
        last_money = re.findall('<span class="ft-gold">￥(.*?)</span>', last, re.S)

        if last_money == []:
            pass
        elif ifsale[num] == '\n                                Purchase Price':

            break
        else:
            last_money = map(float, last_money)
            last_min = min(last_money)
            if float(now_moneys[num]) < last_min:
                url='https://www.c5game.com/csgo/{}/S.html?page=1&flag=&sort=1'.format(i)
                print(url)
                print('名称:', name[num])
                print('现价:', now_moneys[num])
                print('历史最低价:', last_min)
                print('--------------------------------------------------------------------------')
                with open('Buy.csv','a',newline='')as f:
                    f=csv.writer(f)
                    f.writerow([name[num],now_moneys[num],last_min,url])

        num += 1

if __name__ == '__main__':
    type=input('请选择类型：\n'
          '1 匕首\n'
          '2 手枪\n'
          '3 步枪\n'
          '4 微型冲锋枪\n'
          '5 重型武器\n'
          '6 手套\n')
    if type=='1':
        type='csgo_type_knife'
        print('开始查找匕首类')
    elif type=='2':
        type='csgo_type_pistol'
        print('开始查找手枪类')
    elif type=='3':
        type='csgo_type_rifle%7Ccsgo_type_sniperrifle'
        print('开始查找步枪类')
    elif type=='4':
        type='csgo_type_smg'
        print('开始查找微型冲锋枪类')
    elif type=='5':
        type='csgo_type_shotgun'
        print('开始查找重型武器类')
    elif type=='6':
        type='type_hands'
        print('开始查找手套类')
    else:
        type = 'csgo_type_knife'
        print('选择类型错误,默认为匕首')
    pool = Pool()
    for i in range(1, 35):
        web = 'https://www.c5game.com/csgo/default/result.html?type={}&page={}'.format(type,i)
        if requests.get(web).status_code == 200:
            print('正在查找第{}页'.format(i))

            pool.apply_async(html, args=(web,))

    pool.close()
    pool.join()
    print('已寻找结束,结果保存为 Buy.csv')
