import pandas as pd
import numpy as np

data = pd.DataFrame(np.random.rand(9,6),columns=list('abcdef'))
# print(data)
# print(data.head())
# print(data.tail())
# print(data.head(2))
# print(data.tail(2))
# print(data.T)
# print(data.columns)
# print(data.index)
# print(data.describe())描述DataFrame的常用信息汇总
# print(data.mean())
# print(data.mean(axis=1))
# print(data.sort_index(axis=1,ascending=False))降序排列
# print(data.sort_values(by='c'))以c行的值排列
# print(data.reindex([1,2,5,8]))=print(data.loc[[1,2,5,8]])
# print(data.reindex([1,2,5,8],columns=['a','b','e','g']))
del data['e']
# print(data)

# print(data.drop(1))
# print(data.drop('b',axis=1))
data1 = pd.DataFrame(np.random.rand(6,4),columns=list('defg'))
# print(data1)
# print(data1+data)
data2=data+data1
# print(data2.dropna(how='all'))
# print(data2.dropna())
# print(data2.dropna(how='all',axis=1))
# print(data2.fillna(2))


