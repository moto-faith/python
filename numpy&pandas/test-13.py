import pandas as pd
import numpy as np
data = pd.DataFrame(np.random.randn(9,6),columns=list('abcdef'))
# print(data)
# print(data.apply(lambda x:x.max()-x.min()))
# print(data.apply(lambda x:x.max()-x.min(),axis=1))
# print(data['a'].apply(lambda x:x+10))
# print(data['a'].map(lambda x:x+10))
# print(data.applymap(lambda x:x+10))
# print(data.sum())
# print(data.sum(axis=1))
# print(data.idxmax())
# print(data.idxmax(axis=1))
# print(data['a'][data.a.idxmax()])
data=pd.DataFrame(np.random.randint(5,10,(5,6)),columns=list('abcdef'))
# print(data)
# print(data.a.unique())
# print(data.a.value_counts())
# print(data['a'].value_counts())
# print(data.a.isin([7,8,9]))
# print(data.a[data.a.isin([7,8,9])])
data = pd.DataFrame(np.random.randn(6,4),index=[['m','m','m','n','n','n'],['a','b','c','d','e','f']])
# print(data)
# print(data.unstack(0).stack())
# print(data.reset_index())

































