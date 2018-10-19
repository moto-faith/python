import requests
import json
import re
from selenium import webdriver
import time


# 在下方输入账号和密码
login = '账号'
password = '密码'


def getParmas():
    print('正在登录')
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get('https://qzone.qq.com/')

    driver.switch_to.frame('login_frame')
    driver.find_element_by_id('switcher_plogin').click()

    driver.find_element_by_id('u').clear()
    driver.find_element_by_id('u').send_keys(login)
    driver.find_element_by_id('p').clear()
    driver.find_element_by_id('p').send_keys(password)

    driver.find_element_by_id('login_button').click()
    time.sleep(2)

    # ---------------获得 gtk
    cookie = {}  # 初始化cookie字典
    for elem in driver.get_cookies():  # 取cookies
        cookie[elem['name']] = elem['value']

    hashes = 5381
    for letter in cookie['p_skey']:
        hashes += (hashes << 5) + ord(letter)
    gtk = hashes & 0x7fffffff

    html = driver.page_source
    qzonetoken = re.search('window\.g_qzonetoken = \(function\(\)\{ try\{return (.*?);\} catch\(e\)',
                           html)  # 从网页源码中提取g_qzonetoken
    qzonetoken = str(qzonetoken[0]).split('\"')[1]
    print('登录成功')

    return gtk, qzonetoken, cookie


g_tk, qzonetoken, cookies = getParmas()

headers = {
    'Host': 'user.qzone.qq.com',
    'Origin': 'https://user.qzone.qq.com',
    'Referer': 'https://user.qzone.qq.com/{}'.format(login),
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
}

r = requests.get(
    'https://user.qzone.qq.com/proxy/domain/taotao.qq.com/cgi-bin/emotion_cgi_msglist_v6?uin={}&ftype=0&sort=0&pos=0&num=20&replynum=100&g_tk={}&callback=_preloadCallback&code_version=1&format=jsonp&need_private_comment=1&qzonetoken={}&g_tk={}'.format(
        login, g_tk, qzonetoken, g_tk),
    cookies=cookies).text
keys = re.findall('"tid":"(.*?)"', r)
for key in keys:
    data = {
        'hostuin': '{}'.format(login),
        'tid': key,
        't1_source': '1',
        'code_version': '1',
        'format': 'fs',
        'qzreferrer': 'https://user.qzone.qq.com/{}'.format(login),
    }
    r = requests.post(
        'https://user.qzone.qq.com/proxy/domain/taotao.qzone.qq.com/cgi-bin/emotion_cgi_delete_v6?qzonetoken={}&g_tk={}'.format(
            qzonetoken, g_tk),
        data=data, cookies=cookies, headers=headers).text
    code = re.findall('"err":{"code":(.*?)}', r)[0]
    if code == '0':
        print('id为: {} 的说说已被删除'.format(key))
    else:
        print('id为: {} 的说说删除出现错误'.format(key))
