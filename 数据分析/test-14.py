from datetime import datetime
import numpy as np
import pandas as pd
now=datetime.now()
# print(now.year,now.month,now.day)
delta=datetime(2018,4,20)-datetime(2018,3,20,10)
# print(delta.days)
# print(delta.seconds)
from datetime import timedelta
start=datetime(2017,8,24)+timedelta(30)
# print(start)
theday=datetime(2017,10,1)
# print(theday)
a=theday.strftime('%Y-%m-%d')
# print(a[:4])
# print(datetime.strptime(a,'%Y-%m-%d'))
# print(pd.to_datetime(['2017/10/1','2017/8/24']))
index=pd.date_range('8/1/2017','8/20/2017')
# print(index)
index=pd.date_range(start='4/1/2018',periods=20)
# print(index)
index=pd.date_range(end='4/1/2018',periods=20)
# print(index)
index=pd.date_range('1/1/2017','12/1/2017',freq='BM')
# print(index)
index=pd.date_range('1/1/2017','12/1/2017',freq='2M')
# print(index)
index=pd.date_range('1/1/2017','12/1/2017',freq='BM')-timedelta(2)#每月最后一天的前两天
# print(index)
index=pd.date_range('1/1/2017','12/1/2017',freq='BM')-timedelta(2,10)#每月最后一天的前两天的前10分
# print(index)
index=pd.date_range('4/1/2018 12:30:30',periods=20)
# print(index)
index=pd.date_range('4/1/2018 12:30:30',periods=5,normalize=True)
# print(index)
ts=pd.Series(np.random.randn(8),index=pd.date_range('10/1/2017',periods=8))
# print(ts)
# print(ts+ts[::2])
ts1=pd.Series(np.random.randn(1000),index=pd.date_range('10/1/2017',periods=1000))
# print(ts1['20171011'])
# print(ts1['2017'].tail())
# print(ts1['10/2017'].tail())
p=pd.period_range('2017/1/1','2017/12/31',freq='M')
# print(p)
s=pd.date_range('1/1/2017','12/1/2017',freq='M')
print(s)













