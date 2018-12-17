#!/usr/local/bin/python3

from GetStockCode import GetStockCode
from GetStockData import GetStockData
import time

if __name__ == '__main__':
    #get current day

    start = '20181127'
    end = '20181127'
    path = './curday/'
    #
    #    #get stock data from start to end date

    #Get the code from GetStockCode feature
    gscobj = GetStockCode()
    code = gscobj.run()

    #Download the data
    gsdobj = GetStockData(code, path)
    gsdobj.downloadStockData(start, end)

#gsdobj.downloadAllStockData()
