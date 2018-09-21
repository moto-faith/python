from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import re
from pyquery import PyQuery as pq
import pymongo


MONGO_URL = 'localhost'
MONGO_DB = 'toutiao'
MONGO_TABLE = 'toutiao'
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)
def search(keywords):
    try:
        browser.get('https://www.taobao.com/')
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#q'))
        )
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
        input.send_keys(keywords)
        submit.click()
        total = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.total'))).text
        total = re.search('(\d+)',total,re.S)
        return int(total.group(1))
    except:
        return search(keywords)

def change_page(i):
    try:
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > input'))
        )
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > div.form > span.btn.J_Submit')))
        input.clear()
        input.send_keys(i)
        submit.click()
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager > div > div > div > ul > li.item.active > span'),str(i)))
        get_product()
    except:
        return  change_page(i)

def get_product():
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items .item')))
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product={
            'image':item.find('.pic .img').attr('src'),
            'name':item.find('.title').text().replace('\n',''),
            'price':item.find('.price').text().replace('\n',''),
            'deal':item.find('.deal-cnt').text()[:-3],
            'shop':item.find('.shop').text(),
            'location':item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)

def save_to_mongo(product):
    try:
        if db[MONGO_TABLE].insert(product):
            print('保存到MongoDB成功',product)
    except Exception:
        print('保存失败',product)

def main(keywords):
    total = search(keywords)
    for i in range(2,total+1):
        change_page(i)
    browser.close()

if __name__ == '__main__':
    keywords = '美食'
    main(keywords)