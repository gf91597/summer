#!/usr/local/bin/python3

from StoreData import StoreData
from DatabaseOps import DatabaseOps
import time

if __name__ == '__main__':

    path = './data/'
    cur_path = './curday/'

    #store stock Data into mysql
    ssoobj = DatabaseOps()
    ssobj = StoreData(ssoobj, 'stock', cur_path)

    ssobj.createDataBase()
    ssobj.storeData()
