#!/usr/local/bin/python3

import pymysql
import re


class DatabaseOps(object):
    """store all stock data into mysql"""

    def __init__(self):
        self.userName = 'root'
        self.passworkd = 'ivanzhu0928'
        self.db = pymysql.connect('localhost', self.userName, self.passworkd, \
                                charset='utf8')
        self.cursor = self.db.cursor()

    def ifExist(self, sql, name):
        self.cursor.execute(sql)
        database = [self.cursor.fetchall()]
        database_list = re.findall('(\'.*?\')', str(database))
        database_list = [re.sub("'", '', each) for each in database_list]
        if name in database_list:
            return 1
        else:
            return 0

    def databaseExist(self):
        sql = "show databases"
        ret = self.ifExist(sql, self.dataBaseName)
        return ret

    def tableExist(self):
        sql = "show tables"
        ret = self.ifExist(sql, self.tableName)
        return ret

    def choseDatabase(self):
        sql = 'use ' + self.dataBaseName
        self.cursor.execute(sql)

    def createDatabase(self, dataBaseName):
        self.dataBaseName = dataBaseName
        if (self.databaseExist() != 1):
            #database not exist
            sql = 'create database ' + self.dataBaseName
            self.cursor.execute(sql)
        else:
            print('database %s exist' % self.dataBaseName)
        self.choseDatabase()

    def createTable(self, tableName, sql):
        self.tableName = tableName
        if (self.tableExist() != 1):
            #database not exist
            self.cursor.execute(sql)
        else:
            print('table  %s exist' % self.tableName)

    def insertStockData(self, sql):
        self.cursor.execute(sql)

    def deleteStockData(self, sql):
        self.cursor.execute(sql)

    def selectStockData(self, sql):
        self.cursor.execute(sql)
        res = self.cursor.fetchall()
        return res

    def closeDataBase(self):
        self.cursor.close()
        self.db.commit()
        self.db.close()
