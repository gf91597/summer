#!/usr/local/bin/python3

from GetStockCode import GetStockCode
from GetStockData import GetStockData
from StoreData import StoreData
from StoreStockOps import StoreStockOps
import time

if __name__ == '__main__':

    #get current day
    #cur_day = time.strftime('%Y%m%d', time.localtime(time.time()))
    #get the stock list
    # gscobj = GetStockCode()
    # codelist = gscobj.run()
    #
    #    #get stock data from start to end date
    #gsdobj = GetStockData(codelist)
    #gsdobj.downloadAllStockData()
    #gsdobj.downloadStockData(end, end)

    #store stock Data into mysql
    ssoobj = StoreStockOps()
    ssobj = StoreData(ssoobj, 'test1', './data/')

    ssobj.createDataBase()
    ssobj.storeData()
