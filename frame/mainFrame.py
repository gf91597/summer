#!/usr/local/bin/python3

import sys
sys.path.append('../API/')

from StockDataAPI import StockDataAPI

import tkinter


class mainFrame(object):
    def __init__(self, api):
        self.title = "Stock Main Frame"
        self.api = api

    def func(self):
        print("test")

    def addButton(self, frame, title, func):
        getCodesBtn = tkinter.Button(frame, text=title, comman=func)
        getCodesBtn.pack()

    def createMainFrame(self):
        mFrame = tkinter.Tk()
        #self.mFrame = mFrame
        mFrame.title(self.title)

        #Set frame size and location
        mFrame.geometry("600x600+400+100")

        #Keep the frame size
        mFrame.resizable(0, 0)

        return mFrame

    def mainFrameLoop(self):
        self.mFrame.mainloop()

    def run(self):
        frame = self.createMainFrame()
        frm = tkinter.Frame(frame)
        frm.pack()
        frm_L = tkinter.Frame(frm)
        self.addButton(frm_L, "下载代码", self.api.getStockCode)
        self.addButton(frm_L, "下载数据", self.api.getStockData)
        self.addButton(frm_L, "存储数据", self.api.storeStockData)
        self.addButton(frm_L, "备份数据", self.api.backupStockData)
        self.addButton(frm_L, "恢复数据", self.api.recoverStockData)
        frm_L.pack(side=tkinter.LEFT)

        frm_R = tkinter.Frame(frm)
        text = tkinter.Text(frm_R, width=60, height=10)
        text.pack()
        str = 'jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjfdlksf s成绩单差福建省垃圾分类数据发垃圾分类快结束了开发建设路口附近案例三分类数据分类卡萨老公还是空间发挥了开始叫对方离开静安寺多了；开发；就是了空间分类考试等级分类考试加分离开静安寺路口附近时离开房间了；按时交付了；数据的分类考试就离开房间爱老师傅吉林省会计法'
        text.insert(tkinter.INSERT, str)

        frm_R.pack(side=tkinter.RIGHT)

        frame.mainloop()


api = StockDataAPI()
obj = mainFrame(api)
obj.run()
