import pandas as pd
import numpy as np
data = pd.DataFrame(np.arange(6).reshape(2,3),index=['xiaoming','xiaoli'],columns=['one','two','three'])
# print(data.unstack())
# print(data.stack())
data=pd.DataFrame({'k1':['one']*3+['two']*2,'k2':[1,1,2,3,3]})
# print(data)
# print(data.duplicated())
# print(data.drop_duplicates())
# print(data.drop_duplicates('k1'))
# print(data.replace(2,np.nan))
# print(data.replace([2,3],np.nan))
data=pd.DataFrame(np.random.randint(1,50,(20,2)),columns=['k1','k2'])
# print(data.head())
bins=[0,10,20,30,40,50]
data1=pd.cut(data.k1,bins,right=False)
# print(data1.value_counts())
data1=pd.cut(data.k1,4)#根据值来划分4组
# print(data1)
data1=pd.qcut(data.k1,4)#根据数量来划分4组
# print(data1.value_counts())










