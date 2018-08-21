import numpy as np
import pandas as pd
f=open('kongnan.csv',encoding='gb18030',errors='ignore')
data = pd.read_csv(f)
# print(data.Location.value_counts()[:10])
data['Date']= data.Date.map(lambda x:x.split('/')[-1])
# print(data.Date.value_counts()[:10])
# print(data.groupby('Date')[['Fatalities']].sum().sort_values(by='Fatalities',ascending=False))
data['taoshenglv']=(data.Aboard-data.Fatalities)/data.Aboard
# print(data['taoshenglv'])
data1=data[['Date','Location','Type','Aboard','Fatalities','taoshenglv']]
# print(data1.describe())
# print(data1[data.Aboard>600])
# print(data.groupby('Location')[['Fatalities']].sum())
# print(data1.groupby('Location')[['taoshenglv']].mean().sort_values(by='taoshenglv',ascending=False))
# print(data.groupby('Type')[['taoshenglv']].mean().sort_values(by='taoshenglv',ascending=False))