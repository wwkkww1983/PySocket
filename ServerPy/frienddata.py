#****************************************************
# 作者：YYC
# 功能：好友管理
# 日期：2017-10-28
#****************************************************

import sqlite3
import globaldef


class FriendData():

    # 构造函数
    def __init__(self):
        self.dataConn()

    # 连接数据库
    def dataConn(self):
        try:
            self.conn = sqlite3.connect("student.db")
            self.cursor = self.conn.cursor()
        except Exception as e:
            print(e.args)

    # 添加好友
    def addFriend(self):
        pass

    # 删除好友
    def subFriend(self):
        pass

    # 查询好友列表
    def selectFriends(self, userName):
        try:
            self.dataConn()

            str  = "select username , name from " + globaldef.TABLEFRIENDDATA + "," +  globaldef.TABLEPERSONDATA

            str +=  "  where " + globaldef.TABLEFRIENDDATA + ".userSecond = " + globaldef.TABLEPERSONDATA

            str +=  ".username" + " and userFirst = '" + userName + "';"

            print(str)

            data = self.cursor.execute(str)
            self.conn.commit()

            return data
        except Exception as e:
            print(e.args)
            return None

    # 查询好友列表
    def selectFriend(self, userName):
        try:
            self.dataConn()

            str = "select username from " + globaldef.TABLEUSER + "  where username like '%" + userName + "%';"
            data = self.cursor.execute(str)
            self.conn.commit()
            return data
        except Exception as e:
            print(e.args)
            return None

    # 好友推荐
    def recommendFriend(self):
        pass
