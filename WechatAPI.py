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
        msgId = root.find('MsgId').text
        msgType = root.find('MsgType').text
        result = {"fromUser":fromUser,"toUser":toUser,"createTime":createTime,"msgId":msgId,"msgType":msgType}
        #拼装文本消息
        if msgType == 'text':
            msgContent = root.find('Content').text.encode('utf-8')
            result["msgContent"] = msgContent.decode('utf-8')
            return result

