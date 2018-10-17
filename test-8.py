import time
from multiprocessing import Pool
import requests
from lxml import etree


def test(i):

    url = 'https://book.douban.com/top250?start={}'.format(i * 25)
    j = i * 25
    spider(url, j)

def spider(url, i):
    htmlText = requests.get(url).text
    selector = etree.HTML(htmlText)
    tds = selector.xpath('//*[@id="content"]/div/div[1]/div/table')

    for td in tds:
        name = td.xpath('./tr/td[2]/div[1]/a/text()')[0]
        auther = td.xpath('./tr/td[2]/p[1]/text()')[0]
        score = td.xpath('./tr/td[2]/div[2]/span[2]/text()')[0]
        print(name,auther,score)

if __name__ == '__main__':
    pool = Pool()
    time3 = time.time()
    for item in range(11):
        pool.apply_async(test, args=(item,))
    pool.close()
    pool.join()

    time4 = time.time()
    print('multiprocess needs ' + str(time4 - time3) + ' s')


    time1=time.time()
    for i in range(11):
        test(i)
    time2=time.time()
    print(str(time2-time1)+'s') 
