import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import matplotlib

ts=pd.Series(np.random.randn(1000),index=pd.date_range('1/1/2000',periods=1000))
ts=ts.cumsum()
# ts.plot(title='qushitu')
# plt.xlabel('time')
# plt.ylabel('length')

df=pd.DataFrame(np.random.randn(1000,4),index=ts.index,columns=list('ABCD'))
df=df.cumsum()
# df.plot()

# df3=pd.DataFrame(np.random.randn(1000,2),columns=['B','C']).cumsum()
# df3['A']=pd.Series(list(range(1000,2000)))
# df3.plot()

# df.iloc[3].plot.bar(rot=0)
# plt.axhline(0,color='k')

df4=pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
# df4.iloc[0].plot.bar(rot=0)

# df4.plot.barh(stacked=True)
df5 = pd.DataFrame({'a':np.random.randn(1000)+1,
                    'b':np.random.randn(1000),
                    'c':np.random.randn(1000)-1})
# df5.plot.hist()
df6 = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
# df6.plot.area()
# df6.plot.bar(stacked=True)
df7= pd.DataFrame(np.random.rand(50,4),columns=['a','b','c','d'])
# ax=df7.plot.scatter(x='a',y='b',color='grey',label='group1')
# df7.plot.scatter(x='c',y='d',color='red',label='group2',ax=ax)
# df6.plot.scatter(x='a',y='b',s=df7['c']*200)

series = pd.Series(np.random.rand(4),index=['a','b','c','d'],name='bitch')
# series.plot.pie(figsize=(8,8))
data8=pd.DataFrame(np.random.rand(4,2),index=['a','b','c','d'],columns=['x','y'])
# data8.plot.pie(figsize=(16,8),subplots=True,legend=False)
data9=pd.DataFrame(np.random.randn(1000,4),index=df.index,columns=list('ABCD'))
df10=data9.cumsum()
fig,axs=plt.subplots(1,2)
df10['A'].plot(ax=axs[0])
df10['B'].plot(ax=axs[1])

plt.show()




