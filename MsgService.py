# -*- coding:utf-8 -*-
from reply import *
class MsgService:
    #获取消息路由，确定由哪个具体的方法来处理消息，也就是设置关键字
    def GetMsgRouter(self,msgDict):
        toUser = msgDict['fromUser']
        fromUser = msgDict['toUser']
        if msgDict['msgType'] == 'text' and msgDict['msgContent'] == "借书":
            return TextMsg(toUser,fromUser,"有人借书拉").send()
        else:
            return TextMsg(toUser,fromUser,msgDict['msgContent']).send()

