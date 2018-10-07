import requests
import json
import re
r = requests.get('http://127.0.0.1:8000/?protocol=2')
ip_ports = json.loads(r.text)
for ips in ip_ports:

    ip = ips[0]
    port = ips[1]
    print(ip,port)
    proxies={
        'http':'http://%s:%s'%(ip,port),
        'https':'http://%s:%s'%(ip,port)
    }
    r = requests.get('https://www.baidu.com/',proxies=proxies)
    r.encoding='utf-8'
    if r.status_code==200:
        print('正常代理：',ip)
    else:
        d = requests.get('http://127.0.0.1:8000/delete?ip={}'.format(ip))
        print('不能使用的代理：',ip)
