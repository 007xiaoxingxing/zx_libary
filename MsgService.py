# -*- coding:utf-8 -*-
from reply import *
import urllib2
import urllib
import json
class MsgService:
    #获取消息路由，确定由哪个具体的方法来处理消息，也就是设置关键字
    def GetMsgRouter(self,msgDict):
        toUser = msgDict['fromUser']
        fromUser = msgDict['toUser']
        if msgDict['msgType'] == 'text' and msgDict['msgContent'] == "借书":
            return TextMsg(toUser,fromUser,"有人借书拉").format()
        elif msgDict['msgType'] == 'text' and msgDict['msgContent'] == "还书":
            return TextMsg(toUser,fromUser,"有人还书拉").format()
        if msgDict['msgType'] == 'text' and msgDict['msgContent'] == "绑定":
            return ArticalMsg(toUser,fromUser).format()
        else:
            #调用图灵机器人接口回复一些其他内容
            tuling_url = "http://www.tuling123.com/openapi/api"
            key = "ad4c133e35c744acb3c707bd27d74e87"
            data = {'key':key,'info':msgDict['msgContent'],'userid':toUser}
            res = urllib2.urlopen(tuling_url,urllib.urlencode(data)).read()
            return TextMsg(toUser,fromUser,json.loads(res)['text']).format()

