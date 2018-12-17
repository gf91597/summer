#!/usr/local/bin/python3

from matplotlib import pyplot as plt
import mpl_finance as mpf
#from matplotlib import finance as mpf
from matplotlib.pylab import date2num
import pandas as pd
import datetime

plt.bar([1, 3, 5, 7, 9], [5, 4, 8, 12, 7], label='graph 1')

plt.bar([2, 4, 6, 8, 10], [4, 6, 8, 13, 15], label='graph 2')

# params

# x: 条形图x轴
# y：条形图的高度
# width：条形图的宽度 默认是0.8
# bottom：条形底部的y坐标值 默认是0
# align：center / edge 条形图是否以x轴坐标为中心点或者是以x轴坐标为边缘

plt.legend()

plt.xlabel('number')
plt.ylabel('value')

plt.title(u'测试例子——条形图')

plt.show()
