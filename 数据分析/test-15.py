import pandas as pd
import numpy as np
from datetime import datetime
rng=pd.date_range('10/1/2017',periods=60)
ts=pd.Series(np.random.randn(60),index=rng)
# print(ts['10/1/2017'])
# print(ts['10/31/2017'])
ts1=ts.resample('m').mean()#把从天取样改为从月取样
# print(ts1)
ts2=ts.resample('M').ohlc()#open开盘价，high最高价，low最低价，close收盘价
# print(ts2)
# print(ts.groupby(lambda x:x.week).mean())

tf = pd.DataFrame(np.random.randn(2,4),
                  index=pd.date_range('2017/10/1',periods=2,freq='W'),#freq='W'间隔为周
                  columns=['a','b','c','d'])
# print(tf)
# print(tf.resample('D').asfreq())#以天为采样频率
# print(tf.resample('D').pad())#用前一个数据填上所有空数据
# print(tf.resample('D').bfill())#用后一个数据填上所有空数据


f=open('kongnan.csv',encoding='gb18030',errors='ignore')
data=pd.read_csv(f,index_col='Date',parse_dates=True)#索引设置为日期,解析为时间序列
print(data.Fatalities.resample('A').sum())#以年为采样频率计算每年的和




