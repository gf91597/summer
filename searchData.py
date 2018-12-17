#!/usr/local/bin/python3

from GetStockCode import GetStockCode
from GetStockData import GetStockData
from StoreData import StoreData
from DatabaseOps import DatabaseOps
import time
import pymysql
import re
import pandas as pd
import os


class SearchData(object):
    """search every stock to find some useful things"""

    def __init__(self):
        self.userName = 'root'
        self.password = 'ivanzhu0928'
        self.db = pymysql.connect('localhost', self.userName, self.password, \
                                charset='utf8')
        self.cursor = self.db.cursor()

    def getCodeList(self):
        obj = GetStockCode()
        self.codeList = obj.run()

    def choseDataBase(self):
        name = 'store2'
        sql = 'use ' + name
        self.cursor.execute(sql)

    def closeDataBase(self):
        self.cursor.close()
        self.db.commit()
        self.db.close()

    def searchLastEle(self, sql):
        #for item in self.codeList:
        #sql = "select slow from stock_600004 where (datediff(sdate , '2018-11-20')=0)"
        print(sql)
        self.cursor.execute(sql)
        result = self.cursor.fetchall()
        return result


obj = SearchData()
obj.choseDataBase()
obj.getCodeList()
sql1 = "select concat_ws(',', skaipan, sshoupan) from stock_600004 where (datediff(sdate , '2018-11-20')=0)"
#sql2 = "select sshoupan from stock_600004 where (datediff(sdate , '2018-11-20')=0)"
res1 = obj.searchLastEle(sql1)
#res2 = obj.searchLastEle(sql2)

print(max(res1))

#res =  res1[0] + res2[0]


#rmax = max(res)
#rmin = min(res)

#print(rmax)
#print(rmin)

#print(rmax - rmin)
