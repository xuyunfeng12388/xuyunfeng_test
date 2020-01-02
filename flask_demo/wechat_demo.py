import time

import xmltodict
from flask import Flask, request, make_response
import hashlib
import random



app = Flask(__name__)


@app.route('/wechat',methods=['GET','POST'])
def wechat():
    # 设置token
    if request.method == 'GET':
        token = '941025xyf'
        data = request.args
        signature = data.get('signature')
        timestamp = data.get('timestamp')
        nonce = data.get('nonce')
        echostr = data.get('echostr')
        temp = [timestamp, nonce, token]
        temp.sort()
        temp = ''.join(temp)
        if (hashlib.sha1(temp).hexdigest() == signature):
            return make_response(echostr)

    if request.method == 'POST':
        message = [
            "你是笨蛋", "丽丽，我喜欢你", "点点，不要不理我", "我想领走你，可以吗？"
        ]
        xml = request.data
        req = xmltodict.parse(xml)['xml']
        if req.get('Content') not in message:
            message.append(req.get('Content'))
            content = "老师，我学会了" + req.get('Content')
        else:
            content = random.choice(message)
        if 'text' == req.get('MsgType'):

            resp = {
                'ToUserName': req.get('FromUserName'),
                'FromUserName': req.get('ToUserName'),
                'CreateTime': int(time.time()),
                'MsgType': 'text',
                'Content': content
            }
            xml = xmltodict.unparse({'xml': resp})
            print(req.get('Content'))
            return xml
        else:
            resp = {
                'ToUserName': req.get('FromUserName', ''),
                'FromUserName': req.get('ToUserName', ''),
                'CreateTime': int(time.time()),
                'MsgType': 'text',
                'Content': content
            }
            xml = xmltodict.unparse({'xml': resp})
            return xml


if __name__ == '__main__':
    app.run(host="172.18.227.119", port=9466)
