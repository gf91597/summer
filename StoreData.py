#!/usr/local/bin/python3

from DatabaseOps import DatabaseOps
import pandas as pd
import os
import datetime
import pymysql


class StoreData(object):
    """Store all Stock data into mySql"""

    def __init__(self, obj, dataBaseName, path):
        self.dataBaseName = dataBaseName
        self.filePath = path
        self.fileList = os.listdir(self.filePath)
        self.obj = obj

    def createDataBase(self):
        self.obj = DatabaseOps()
        self.obj.createDatabase(self.dataBaseName)

    def getAllFileCnt(self):
        count = 0
        for item in self.fileList:
            count += 1
        return count

    def createTable(self, tableName, sql):
        self.obj.createTable(tableName, sql)

    def storeData(self):
        has_cnt = 0
        for fileName in self.fileList:
            try:
                data = pd.read_csv(self.filePath + fileName, encoding="gbk")
                length = len(data)
                has_cnt += 1
                if length != 0:
                    re = []
                    record = tuple(data.loc[0])
                    re.append(record[1])
                    re.append(record[2])
                    res = tuple(re)

                    #store stocks code and name
                    selectSql = "select * from stocks where (stock_code = '" + fileName[
                        0:6] + "')"
                    ret = self.obj.selectStockData(selectSql)
                    if not ret:
                        #print('insert')
                        storeSql = "insert into stocks (stock_code, stock_name) values (%s', '%s')" % res
                        #print(storeSql)
                        self.obj.insertStockData(storeSql)

                # cur_day = datetime.datetime.now().strftime('%Y-%m-%d')
                # sel = "select stock_code from stockdata where (datediff(stock_date,'" + cur_day + "'))"
                # a = self.obj.selectStockData(sel)

                    print(fileName, has_cnt, length)
                    for i in range(0, length):
                        rdata = tuple(data.loc[i])
                        sql = "insert into stockdata (\
                                stock_date, stock_code, stock_name, \
                                stock_shoupan, stock_high, stock_low, \
                                stock_kaipan, stock_qianshou, stock_zhangdiee, \
                                stock_zhangdiefu, stock_huanshoulv, \
                                stock_chengjiaoliang, stock_chengjiaojine, \
                                stock_total, stock_liutong) values \
                                ('%s',%s','%s',%s,%s,%s,%s,%s,%s,%s,%s,%s,\
                                %s,%s,%s)" % rdata
                        sql = sql.replace('nan', 'null').replace(
                            'None', 'null').replace('none', 'null')
                        self.obj.insertStockData(sql)

                else:
                    continue
            except:
                print('current error fileName ', fileName)
                break

            #sql = "insert into stocks (stock_code, stock_name) values ('%s', '%s')" % (
            #    record[1], record[2])

        #for fileName in self.fileList:
        #    time.sleep(0.1)
        #    has_cnt += 1
        #    data = pd.read_csv(self.filePath + fileName, encoding="gbk")

        #    length = len(data)
        #    print(length)
        #    #for i in range(0, length):
        #    print(record1[1], record1[2])

        self.obj.closeDataBase()
