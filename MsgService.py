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
            return ArticalMsg(toUser,fromUser,'哟？你要借书吗?','快点我，点我，我带你飞!','http://lib.star-chen.com/borrow?openid=').format()
        elif msgDict['msgType'] == 'text' and msgDict['msgContent'] == "还书":
            return TextMsg(toUser,fromUser,"有人还书拉").format()
        elif msgDict['msgType'] == 'text' and msgDict['msgContent'] == "绑定":
            return ArticalMsg(toUser,fromUser,'点我进入绑定流程~','霞姐说了,如果你不绑定是没法借书滴','http://lib.star-chen.com/bind?openid=').format()
        elif msgDict['msgType'] == 'text' and msgDict['msgContent'] == "审核" and msgDict['fromUser'] == 'oy1IAs2qSA2K9Ilx0UBoe117V6XI':
            return ArticalMsg(toUser,fromUser,'看看都有谁借书了','霞妹妹,霞妹妹,我爱你','http://lib.star-chen.com/check?openid=').format()
        else:
            #调用图灵机器人接口回复一些其他内容
            tuling_url = "http://www.tuling123.com/openapi/api"
            key = "ad4c133e35c744acb3c707bd27d74e87"
            data = {'key':key,'info':msgDict['msgContent'],'userid':toUser}
            res = urllib2.urlopen(tuling_url,urllib.urlencode(data)).read()
            return TextMsg(toUser,fromUser,json.loads(res)['text']).format()

