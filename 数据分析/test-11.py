
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

import matplotlib

f=open('renli.csv')
data = pd.read_csv(f)
data=data[['satisfaction_level','average_montly_hours','time_spend_company','Work_accident','sales', 'salary']]
dic={'satisfaction_level':'manyidu','average_montly_hours':'yue_gongshi','time_spend_company':'zuoban','Work_accident':'shigu','sales':'leixing', 'salary':'gongzi'}
data.columns=data.columns.map(lambda x:dic.get(x))
# print(data.leixing.unique())
# print(data.groupby('leixing').size())
# print(data.groupby(['leixing','gongzi'])['yue_gongshi'].mean())
# print(data.groupby(['leixing','gongzi'])['yue_gongshi'].mean().unstack())
data1=data.groupby(['leixing','gongzi'])['yue_gongshi'].mean().unstack()
# data1.plot.bar(stacked = True,rot=60)
def zb(group):
    g=group['manyidu'].sort_values(ascending=False)
    return g[:5]
# print(data.groupby(['gongzi','leixing']).apply(zb))
data1=data.groupby(['leixing','gongzi'])['manyidu'].mean().unstack()
data1.plot(rot=60)

cat = pd.cut(data.manyidu,4)
# print(cat.value_counts())
# print(data.groupby(['leixing',cat]).size().unstack())
def xg(group):
    return group['manyidu'].corr(group['yue_gongshi'])
# print(data.groupby(['gongzi','leixing']).apply(xg))
print(data.groupby(['gongzi','leixing']).apply(xg).unstack(0))

# plt.show()



