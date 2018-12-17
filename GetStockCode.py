#!/usr/local/bin/python3

#导入需要使用到的模块
import urllib
import re
import pandas as pd
import pymysql
import os
import time


class GetStockCode(object):
    """get all stock code """

    def __init__(self):
        self.url = 'http://quote.eastmoney.com/stocklist.html'

    #get the store list page
    def getStockHtml(self):
        html = urllib.request.urlopen(self.url).read()
        html = html.decode('gbk')
        return html

    #scrapy the store list of sh6x and sz0x
    def getShStockList(self, html):
        shs = r'<li><a target="_blank" href="http://quote.eastmoney.com/[s][h|z]([6|0].*?).html">'
        shpat = re.compile(shs)
        hlst = shpat.findall(html)
        shlst = []
        for lst in hlst:
            try:
                shlst.append(lst)
            except:
                continue
        return shlst

    def saveStockCode(self):
        html = self.getStockHtml()
        shlist = self.getShStockList(html)
        shlist.remove('038016')
        shlist.remove('038014')
        shlist.remove('002525')
        shlist.remove('002257')
        shlist.remove('031005')
        shlist.remove('038017')
        shlist.remove('038015')
        shlist.remove('038011')
        shlist.remove('031007')
        fp = open('saveCode.csv', 'w+')
        for i in range(len(shlist)):
            fp.writelines(str(shlist[i] + '\n'))
        fp.close()

        return shlist

    def run(self):
        tmp = []
        f = open('./saveCode.csv', 'r+')
        lines = f.readlines()
        for line in lines:
            tmp.append(line)
        #for item in range(len(line))
        f.close()

        code = []
        for item in tmp:
            code.append(item[0:6])
        return code
