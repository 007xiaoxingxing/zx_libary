# -*- coding:utf-8 -*-
import xml.etree.cElementTree as ET
class WechatAPI:
    def __init__(self):
        print "init"

    #解析微信服务器更传回的xml
    def ParseWechatXML(self,wechatXML):
        root = ET.fromstring(wechatXML)
        fromUser = root.find('FromUserName').text
        toUser = root.find('ToUserName').text
        createTime = root.find('CreateTime').text
        msgType = root.find('MsgType').text
        result = {"fromUser":fromUser,"toUser":toUser,"createTime":createTime,"msgType":msgType}
        #拼装文本消息
        if msgType == 'text':
            msgContent = root.find('Content').text
            msgId = root.find('MsgId').text
            result["msgContent"] = msgContent
            result["msgId"] = msgId
            return result
        #拼装事件消息
        if msgType == 'subscribe':
            result['event'] = 'subscribe'
            return result


