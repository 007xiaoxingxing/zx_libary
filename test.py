# -*- coding:utf-8 -*-
import urllib2
import urllib
import json
import os
import time
from SQLHelper import *
"""
tuling_url = "http://www.tuling123.com/openapi/api"
key = "ad4c133e35c744acb3c707bd27d74e87"
data = {'key':key,'info':'我是谁'}
res = urllib2.urlopen(tuling_url,urllib.urlencode(data)).read()
print json.loads(res)['text']
"""
path = os.path.realpath(__file__)
print path
sqlHelper = SQLHelper()
sqlHelper.DBInit()
sqlHelper.AddUser("张三","13800138000","vasdflasdlfjalsdkfjljl")
#sqlHelper.GetUserID("vasdflasdlfjalsdkfjljl")
currentTime = int(time.time())
print sqlHelper.BorrowBook(1,1,currentTime)
#print sqlHelper.BackBook(1,1,currentTime)
'''
books = sqlHelper.ExcuteSQL("select * from book")
for book in books:
    print book
'''
result = sqlHelper.ExcuteSQL("select user_id,borrow_time from borrow_list where book_id={0} and back_time = 0 ".format(1))
print result[0][1]
print sqlHelper.ExcuteSQL("select name from user where id = {0}".format(1))[0][0]
