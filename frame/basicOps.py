#!/usr/local/bin/python3

import tkinter
import sys

sys.path.append('../API/')
from StockDataAPI import StockDataAPI
from mainFrame import mainFrame


class basicOps(object):
    def __init__(self, api):
        self.api = api

    def addButton(self, title, func):
        obj = mainFrame()
        mFrame = obj.createMainFrame()
        self.mobj = obj
        self.mFrame = mFrame
        getCodesBtn = tkinter.Button(
            mFrame, text=title, comman=func, width=10, height=10)
        getCodesBtn.pack(side=tkinter.RIGHT)

        #obj.mainFrameLoop()

    def addFrame(self, title):
        pass

    def mainFrameLoop(self):
        self.mobj.mainFrameLoop()


api = StockDataAPI()

obj = basicOps(api)

obj.addButton("haha", api.getStockCode)

obj.mainFrameLoop()
