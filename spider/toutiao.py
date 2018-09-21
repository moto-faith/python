import re
import requests
import json
import pymongo
from urllib.parse import urlencode
from bs4 import BeautifulSoup

MONGO_URL = 'localhost'
MONGO_DB = 'toutiao'
MONGO_TABLE = 'toutiao'


client = pymongo.MongoClient(MONGO_URL, connect=False)
db = client[MONGO_DB]

def get_html(offset,keyword):
    html = 'https://www.toutiao.com/search_content/?'
    data = {
        'offset': offset,
        'format': 'json',
        'keyword': keyword,
        'autoload': 'true',
        'count': '20',
        'cur_tab': '3',

    }
    url = html+urlencode(data)
    try:
        response = requests.get(url)
        if response.status_code==200:
            return response.text
        return None
    except ConnectionError:
        return None

def get_parse(text):
    try:
        data = json.loads(text)
        if data and 'data' in data.keys():
            for item in data.get('data'):
                yield item.get('article_url')
    except:
        pass

def get_page_detil(url):
    try:
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
        }
        response = requests.get(url,headers=headers)
        if response.status_code==200:
            return response.text
        return None
    except:
        return None

def save_imag(images,title):
    i=0
    for image in images:
        content = requests.get(image).content
        with open('{}_{}.jpg'.format(title,i),'wb')as f:
            f.write(content)
        i+=1

def get_img(html,url):
    images_pattern = re.compile('gallery: JSON.parse\("(.*)"\)', re.S)
    soup = BeautifulSoup(html, 'lxml')
    result = soup.select('title')
    title = result[0].get_text() if result else ''
    result = re.search(images_pattern, html)
    data = json.loads(result.group(1).replace('\\', ''))
    sub = data.get('sub_images')
    images = [item.get('url') for item in sub]

    save_imag(images,title)
    return {
        'title':title,
        'url':url,
        'images':images
    }

def save_to_mongo(result):
    if db[MONGO_TABLE].insert(result):
        print('Successfully Saved to Mongo', result)
        return True
    return False

def main():
    text = get_html(offset=0,keyword='街拍')
    urls = get_parse(text)
    for url in urls:
        html = get_page_detil(url)
        result = get_img(html,url)
        if result: save_to_mongo(result)


if __name__ == '__main__':
    main()



