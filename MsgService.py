# -*- coding:utf-8 -*-
import tornado.web
import time
class MsgService(tornado.web.RequestHandler):
    def __int__(self):
        pass
    #获取消息路由，确定由哪个具体的方法来处理消息，也就是设置关键字
    def GetMsgRouter(self,msgDict):
        if msgDict['msgType'] == 'text':
            createTime = int(time.time())
            #print self.render("msgxml/text_msg.xml",toUser = msgDict['fromUser'],fromUser = msgDict['toUser'],createTime = createTime,msgContent=msgDict['msgContent'])
            #print self.render_string("msgxml/text_msg.xml")