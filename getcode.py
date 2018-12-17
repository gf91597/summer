#!/usr/local/bin/python3

from GetStockCode import GetStockCode

if __name__ == '__main__':
    #cur_day = time.strftime('%Y%m%d', time.localtime(time.time())
    #get the stock list
    gscobj = GetStockCode()
    codelist = gscobj.run()
