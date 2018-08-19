import pandas as pd
import numpy as np
data1 = pd.DataFrame({'one':['a','b','a','a','e','f'],'two':range(6)})
data2 = pd.DataFrame({'one':['a','b','c','d'],'two':range(10,14)})
# print(data2)
data = pd.merge(data1,data2,on='one')
# print(data)
data3=pd.DataFrame({'one1':['a','b','a','a','e','f'],'two1':range(6)})
data4=pd.DataFrame({'one2':['a','b','c','d'],'two':range(10,14)})
# print(data3)
# print(data4)
data5=pd.merge(data3,data4,left_on='one1',right_on='one2')
# print(data5)
data5=pd.DataFrame({'one':['a','b','a','a','e','f'],'two1':range(6)})
data6=pd.DataFrame({'one':['a','b','c','d'],'two2':range(10,14)})
data7=pd.merge(data5,data6)
# print(data7)
data7=pd.merge(data5,data6,how='outer')
# print(data7)
data7=pd.merge(data5,data6,how='right')
# print(data7)
data7=pd.merge(data5,data6,how='left')
# print(data7)
data8=pd.DataFrame(np.random.randn(3,4),columns=['a','b','c','d'])
data9=pd.DataFrame(np.random.randn(2,3),columns=['b','d','a'])
data10=pd.concat([data8,data9])
# print(data10)
data10=pd.concat([data8,data9],ignore_index=True)
# print(data10)
data10.append(pd.Series[1,2,3],index=['a','b','d'],ignore_index=True)




































