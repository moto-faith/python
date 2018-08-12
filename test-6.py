import os
import requests
# 'http://image.voltmemo.com/zuizui/lesson/zz_lesson/brcj2_haruka_v1.0_ppt/25/ppt32.jpg '
for i in range(25,49):
    urls='http://image.voltmemo.com/zuizui/lesson/zz_lesson/brcj2_haruka_v1.0_ppt/{}/'.format(i)
    dir = '日语/第'+str(i)+'课'
    os.makedirs(dir)
    for k in range(1,40):
        html=urls+'ppt{}.jpg'.format(k)
        r=requests.get(html)
        if str(r)=='<Response [200]>':
            print('正在下载:'+html)
            with open('日语/第'+str(i)+'课/'+str(k)+'.jpg','ab')as f:
                f.write(r.content)




