#!/usr/local/bin/python3

from matplotlib import pyplot as plt
import mpl_finance as mpf
#from matplotlib import finance as mpf
from matplotlib.pylab import date2num
import pandas as pd
import datetime

#%matplotlib inline

quotes = []
#stock = pd.read_csv('./data/600000.csv', index_col=0, encoding="gbk")
stock = pd.read_csv('./600000.csv', encoding="gbk")

length = len(stock)

print(stock.loc[0])
print(stock.loc[1])

#2018-11-20
for row in range(0, length):
    if row == 0:
        sdate = str(stock.loc[row, 'trade_date'])
        print(sdate)
        sdate_change_format = sdate[0:4] + '-' + sdate[5:7] + '-' + sdate[8:]
        #print(sdate_change_format)
        sdate_num = date2num(
            datetime.datetime.strptime(sdate_change_format,
                                       '%Y-%m-%d'))  #日期需要特定形式，这里进行转换
        sdate_plt = sdate_num
    else:
        sdate_plt = sdate_num - row

    sopen = stock.loc[row, 'open']
    shigh = stock.loc[row, 'high']
    slow = stock.loc[row, 'low']
    sclose = stock.loc[row, 'close']
    datas = (sdate_plt, sopen, shigh, slow,
             sclose)  # 按照 candlestick_ohlc 要求的数据结构准备数据
    quotes.append(datas)

fig, ax = plt.subplots(facecolor=(0, 0.3, 0.5), figsize=(12, 8))
fig.subplots_adjust(bottom=0.1)
ax.xaxis_date()
plt.xticks(rotation=45)  #日期显示的旋转角度
plt.title('600000')
plt.xlabel('time')
plt.ylabel('price')
mpf.candlestick_ohlc(
    ax, quotes, width=0.7, colorup='r',
    colordown='green')  # 上涨为红色K线，下跌为绿色，K线宽度为0.7
plt.grid(True)
ax.xaxis_date()
ax.autoscale_view()
plt.setp(plt.gca().get_xticklabels(), rotation=30)
plt.show()
