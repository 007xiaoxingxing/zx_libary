# -*- coding:utf-8 -*-
import sqlite3
import os


class SQLHelper:
    dbName = "lib.sqlite3"

    def __init__(self):
        pass

    # 数据库初始化
    def DBInit(self):
        # 检测数据库文件是否存在，若不存在则进行表的创建
        if (os.path.exists(self.dbName)):
            return
        # 创建用户表
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
        bookTable = '''

        CREATE TABLE `book` (

          `id` INTEGER PRIMARY KEY AUTOINCREMENT,
          `book_name` TEXT,
          `book_des` TEXT, /*书籍简要描述*/
          `book_status` INTEGER DEFAULT 0, /*书籍在架状态，0-在架，1-已外借*/
          `book_photo` TEXT

        );

        '''

        borrowTable = '''

            CREATE TABLE `borrow_list` (
              `id` INTEGER PRIMARY KEY AUTOINCREMENT,
              `user_id` INTEGER,
              `book_id` INTEGER,
              `borrow_time` NUMERIC,
              `back_time` NUMERIC DEFAULT 0,
              `checked` INTEGER DEFAULT 0

            );

        '''

        checkTable = '''

            CREATE TABLE `borrow_check` (

              `id` INTEGER PRIMARY KEY AUTOINCREMENT,
              `check_type` INTEGER DEFAULT 0, /*0-借书，1-还书*/
              `borrow_list_id` INTEGER ,
              `checked` INTEGER DEFAULT 0 /*0-未审核，1-已审核*/

            )
        '''

        books = open('books.txt')
        line = books.readline()
        cu.execute(userTable)  # 创建用户表
        cu.execute(bookTable)  # 创建书籍表
        cu.execute(checkTable)  # 创建管理员审核表
        cu.execute(borrowTable)  # 创建借阅关系表
        # add a test book
        #cu.execute(books)
        while line:
            cu.execute(line)
            line = books.readline()
        books.close()
        conn.commit()
        conn.close()
        pass

    # 执行sql语句，返回结果
    def ExcuteSQL(self, sql):
        conn = self.GetConn()
        cur = conn.cursor()
        try:
            cur.execute(sql)
            return cur.fetchall()
        except Exception,e:
            print e
            return "error"
        finally:
            conn.commit()
            conn.close()
    # 添加新用户
    def AddUser(self, name, phone, openid):
        conn = self.GetConn()
        cur = conn.cursor()
        addSQL = '''
            INSERT INTO user(name,phone,openid) VALUES("{0}","{1}","{2}")
        '''
        sql = addSQL.format(name, phone, openid)
        try:
            cur.execute(sql)
        except Exception, e:
            print e
            if str(e) == "column openid is not unique":
                return "您已经绑定过了"
        finally:
            conn.commit()
            conn.close()
        return "success"

    # 借书的数据库插入函数
    def BorrowBook(self, userID, bookID, borrowTime):
        borrowSQL = '''
            INSERT INTO borrow_list(user_id, book_id, borrow_time, back_time) VALUES({0}, {1}, {2}, {3});
        '''
        updateBook = '''
            update book set book_status = 1 where id = {0};
        '''
        insertCheckTable = '''

            INSERT INTO borrow_check(check_type,borrow_list_id,checked) VALUES(0,{0},0);
        '''
        updateBook = updateBook.format(bookID)
        borrowSQL = borrowSQL.format(userID, bookID, borrowTime, 0)
        conn = self.GetConn()
        cur = conn.cursor()
        try:
            cur.execute(borrowSQL)
            cur.execute(updateBook)
            last_id = cur.execute("SELECT LAST_INSERT_ROWID() FROM borrow_list").fetchone()[0]
            print insertCheckTable.format(last_id)
            cur.execute(insertCheckTable.format(last_id))
        except Exception, e:
            print e
            return "error"
        finally:
            conn.commit()
            conn.close()
        return "success"

    # 归还书籍
    def BackBook(self, userID, bookID, backTime):
        updateBookList = '''

            update borrow_list set back_time = {0} where user_id ={1} and book_id={2} and back_time=0;
        '''
        updateBook = '''
            update book set book_status = 0 where id = {0};
        '''
        insertCheckTable = '''

            INSERT INTO borrow_check(check_type,borrow_list_id,checked) VALUES(1,{0},0);
        '''

        updateBook = updateBook.format(bookID)
        updateBookList = updateBookList.format(backTime, userID, bookID)
        conn = self.GetConn()
        cur = conn.cursor()
        try:
            cur.execute(updateBookList)
            cur.execute(updateBook)
            print "select id from borrow_list where user_id={0} and book_id={1} and back_time={2}".format(userID,
                                                                                                          bookID,
                                                                                                          backTime)
            last_id = cur.execute(
                "select id from borrow_list where user_id={0} and book_id={1} and back_time={2}".format(userID, bookID,
                                                                                                        backTime)).fetchone()[
                0]
            cur.execute(insertCheckTable.format(last_id))
        except Exception, e:
            print e
            return "error"
        finally:
            conn.commit()
            conn.close()
        return "success"

    # 根据openid获取用户id
    def GetUserID(self, openID):
        conn = self.GetConn()
        cur = conn.cursor()
        cur.execute("select id from user where openid=\"%s\"" % openID)
        id = cur.fetchone()[0]
        return id

    # 获取数据库连接
    def GetConn(self):
        conn = sqlite3.connect(self.dbName)
        return conn
