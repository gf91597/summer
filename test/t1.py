#!/usr/local/bin/python3

from matplotlib import pyplot as plt
import mpl_finance as mpf
#from matplotlib import finance as mpf
from matplotlib.pylab import date2num
import pandas as pd
import datetime

salary = [2500, 3300, 2700, 5600, 6700, 5400, 3100, 3500, 7600, 7800,
          8700, 9800, 10400]

group = [1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 11000]


plt.hist(salary, group, histtype='bar', rwidth=0.8)

plt.legend()

plt.xlabel('salary-group')
plt.ylabel('salary')

plt.title(u'测试例子——直方图')

plt.show()
