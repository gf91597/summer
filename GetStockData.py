#!/usr/local/bin/python3

#导入需要使用到的模块
import urllib
import re
import pandas as pd
import pymysql
import os
import time


class GetStockData(object):
    """get all store Data or chose one day or some days data """

    def __init__(self, code, path):
        self.code = code
        self.date = time.strftime('%Y%m%d', time.localtime(time.time()))
        self.path = path
        self.flagfile = './getflag'

    def pathExist(self):
        if (os.path.exists(self.path)):
            print('%s exists' % self.path)
            pass
        else:
            os.mkdir(self.path)

    def flagFileExist(self):
        if (os.path.exists(self.flagfile)):
            return True
        else:
            return False

    def readFlagFile(self):
        if (self.flagFileExist()):
            f = open(self.flagfile, 'r')
            cnt = f.read()
            f.close()
            return cnt
        else:
            return 0

    def writeFlagFile(self, cnt):
        f = open(self.flagfile, 'w')
        f.write(str(cnt))
        f.close()

    def removeFlagFile(self):
        if (self.flagFileExist()):
            os.remove(self.flagfile)

    #download history stock data
    def downloadAllStockData(self):
        self.pathExist()
        for lst in self.code:
            print("starting get stock num is %s data" % (lst))
            time.sleep(0.1)
            if lst[0] == '6':
                url = 'http://quotes.money.163.com/service/chddata.html?code=0'+lst+\
                        '&end='+self.date+'&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'
            else:
                url = 'http://quotes.money.163.com/service/chddata.html?code=1'+lst+\
                    '&end='+self.date+'&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'
            #print(url)
            #C:\ImageSave\LALA%s.jpg' % x
            urllib.request.urlretrieve(url, self.path + '%s.csv' % lst)

    #download current date stock data
    def downloadStockData(self, start, end):
        self.pathExist()
        cnt = int(self.readFlagFile())

        for cnt in range(cnt, len(self.code)):
            self.writeFlagFile(cnt)
            lst = self.code[cnt]
            print("starting get %s data" % (lst))
            if lst[0] == '6':
                url = 'http://quotes.money.163.com/service/chddata.html?code=0'+lst+\
                        '&start='+start+'&end='+end+'&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'
            else:
                url = 'http://quotes.money.163.com/service/chddata.html?code=1'+lst+\
                    '&start='+start+'&end='+end+'&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP'
            urllib.request.urlretrieve(url, self.path + '%s.csv' % lst)

        self.removeFlagFile()
