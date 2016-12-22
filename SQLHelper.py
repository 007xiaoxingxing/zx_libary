# -*- coding:utf-8 -*-
import sqlite3
import os

class SQLHelper:
    dbName = "lib.sqlite3"
    def __init__(self):
        pass
    #数据库初始化
    def DBInit(self):
        #检测数据库文件是否存在，若不存在则进行表的创建
        if(os.path.exists(self.dbName)):
            return
        #创建用户表
        conn = sqlite3.connect(self.dbName)
        cu = conn.cursor()
        userTable = '''
        CREATE TABLE `user` (
            `id`	INTEGER PRIMARY KEY AUTOINCREMENT,
            `name`	TEXT,
            `phone`	NUMERIC,
            `openid` TEXT UNIQUE
            );
       '''
        cu.execute(userTable)
        pass

    #执行sql语句，返回结果
    def ExcuteSQL(self,sql):
        pass

    #添加新用户
    def AddUser(self,name,phone,openid):
        conn = self.GetConn()
        cur = conn.cursor()
        addSQL = '''
            INSERT INTO user(name,phone,openid) values("{0}","{1}","{2}")
        '''
        sql = addSQL.format(name,phone,openid)
        try:
            cur.execute(sql)
        except Exception, e:
            print e
            if str(e) == "column openid is not unique":
                return "亲，你已经绑定过了"
        conn.commit()
        conn.close()
        return "success"
    #获取数据库连接
    def GetConn(self):
        conn = sqlite3.connect(self.dbName)
        return conn