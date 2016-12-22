# -*- coding:utf-8 -*-
import tornado.web
import tornado.ioloop
import hashlib
from WechatAPI import *
from MsgService import *
from reply import *

class MainHandler(tornado.web.RequestHandler):
    def post(self):
        wechatXML = self.request.body
        API = WechatAPI()
        msgService = MsgService()
        dictMsg = API.ParseWechatXML(wechatXML)
        toUser = dictMsg['fromUser']
        fromUser = dictMsg['toUser']
        res = msgService.GetMsgRouter(dictMsg)
        print res
        self.write(res)
    #处理来自微信服务器的get请求，即第一次的认证请求
    def get(self):
        signature = self.get_argument('signature')
        timestamp = self.get_argument('timestamp')
        nonce = self.get_argument('nonce')
        echostr = self.get_argument('echostr')
        token = "xingxing"

        list = [token, timestamp, nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, list)
        hashcode = sha1.hexdigest()
        if hashcode == signature:
            self.write(echostr)
def main_app():
    return tornado.web.Application([
        (r'/',MainHandler),
    ])
if __name__ == "__main__":
    app = main_app()
    app.listen(81)
    tornado.ioloop.IOLoop.instance().start()