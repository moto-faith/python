import requests
import json
import itchat

# itchat.auto_login(hotReload=True)
#
#
# users=itchat.search_friends("好友")# 找到某好友发信息
# userName= users[0]['UserName']
# print(userName)
# itchat.send('你好',toUserName=userName)

def auto_chat(text):
    data = {
        "perception": {
            "inputText": {
                "text": text
            }
        },
        "userInfo": {
            "apiKey": "dde9f4256d5849c18f98821eaf908db4",
            "userId": '123',
        }
    }
    req = json.dumps(data).encode('utf8')
    r = requests.post('http://openapi.tuling123.com/openapi/api/v2', data=req).text
    print(r)
    r=json.loads(r)['results']
    for resutl in r:
        return resutl['values']['text']

@itchat.msg_register('Text',isGroupChat=False)
def text_reply(msg):
    content = msg['Content']
    fromuser = msg['FromUserName']
    message = auto_chat(content)
    itchat.send(message,fromuser)

itchat.auto_login(hotReload=True)
itchat.run()