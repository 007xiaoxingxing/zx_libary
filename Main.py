# -*- coding:utf-8 -*-
from WechatAPI import *
from MsgService import *
from SQLHelper import *
import hashlib
import sys
import json
import time
import tornado.web
import tornado.ioloop



#微信消息的主入口函数
class MainHandler(tornado.web.RequestHandler):
    def post(self):
        wechatXML = self.request.body
        API = WechatAPI()
        msgService = MsgService()
        dictMsg = API.ParseWechatXML(wechatXML)
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
#处理绑定操作的handler
class BindHandler(tornado.web.RequestHandler):
    def get(self):
        openid = self.get_argument('openid')
        self.render("bind.html",openid=openid)
    def post(self):
        #取得用户提交的json字符串，取出参数
        postBody = json.loads(self.request.body)
        userName = postBody['user']
        userPhone = postBody['phone']
        userOpenID = postBody['openid']
        #将数据插入sqlite数据库中
        sqlHelper = SQLHelper()
        sqlHelper.DBInit()
        bindResult = sqlHelper.AddUser(userName,userPhone,userOpenID)
        self.write(bindResult)
#处理借书请求的Handler
class BorrowBookHandler(tornado.web.RequestHandler):
    def get(self):
        openID = self.get_argument('openid')
        sqlHelper = SQLHelper()
        books = sqlHelper.ExcuteSQL("select * from book")
        self.render('borrow.html',book_list = books,openid=openID)
    def post(self):
        postBody = json.loads(self.request.body)
        bookID = postBody['bookID']
        userOpenID = postBody['openID']
        currentTime = int(time.time())
        sqlHelper = SQLHelper()
        userID = sqlHelper.GetUserID(userOpenID)
        result = sqlHelper.BorrowBook(userID,bookID,currentTime)
        self.write(result)
#处理还书请求Handler
class BackBookHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("????懵逼")
    def post(self):
        postBody = json.loads(self.request.body)
        bookID = postBody['bookID']
        userOpenID = postBody['openID']
        currentTime = int(time.time())
        sqlHelper = SQLHelper()
        userID = sqlHelper.GetUserID(userOpenID)
        result = sqlHelper.BackBook(userID,bookID,currentTime)
        self.write(result)
#查询书籍的节约情况
class BorrowInfoHandler(tornado.web.RequestHandler):
    def get(self):
        sqlHelper = SQLHelper()
        bookid = self.get_argument('bookid')
        result = sqlHelper.ExcuteSQL("select user_id,borrow_time from borrow_list where book_id={0} and back_time = 0 ".format(bookid))
        print result

#个人中心
class PersonHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('person.html')
    def post(self):
        pass
def main_app():
    return tornado.web.Application([
        (r'/',MainHandler),
        (r'/bind',BindHandler),
        (r'/borrow',BorrowBookHandler),
        (r'/back',BackBookHandler),
        (r'/person',PersonHandler),
        (r'/borrowInfo',BorrowInfoHandler)
    ])
if __name__ == "__main__":
    reload(sys)
    sys.setdefaultencoding('utf8')
    app = main_app()
    app.listen(81)
    tornado.ioloop.IOLoop.instance().start()