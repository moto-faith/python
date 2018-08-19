import pandas as pd
import numpy as np
s=pd.Series([1,2,3,4])
# print(s)
s=pd.Series([1,3,5,7],index=['a','b','c','d'])
# print(s)
# print(s.index)
# print(s.values)
# print(s['a'])
# print(s[['a','b']])
# print(s[s>4])
# print(s*4)
# print(np.mean(s))平均值
# print(s.mean())
# print(1 in s.values)
# print('a' in s.index)
b=pd.Series({'a':1,'b':2,'c':3})
# print(b)
b=pd.Series({'a':1,'b':2,'c':3},index=['a','c','d'])
# print(b)
# print(pd.isnull(b))
# print(pd.notnull(b))
c=pd.Series({'a':1,'b':2,'c':3})
d=pd.Series({'a':1,'b':4,'e':5})
# print(c+d)

data = pd.DataFrame({'a':[1,2,3,4],
                     'b':pd.Series([1]*4,dtype='float32'),
                     'c':np.array([3]*4)})
# print(data)

xuhao =['one','two','three','four','five','six']
df = pd.DataFrame(np.random.randn(6,4),index=xuhao,columns=list('abcd'))
# print(df)
# print(df.columns)
# print(df.index)
# print(df['a'])
# print(df[['a','c','d']])
# print(df[:2])
# print(df[2:3])
# print(df.loc['one'])
# print(df.loc[['one','six']])
# print(df.loc[['one','six'],['b','c']])
# print(df.loc[:,['b','c']])
# print(df.loc['two','c'])
# print(df.iloc[3])
# print(df.iloc[1:3,:2])
# print(df.iloc[2,3])
# print(df[df>0])
# print(df[df['a']>0])
df['a']=3
# print(df)
df['d']=np.arange(6)
# print(df)
df['e']=pd.Series([1,2,3,4,5],index=['one','two','three','four','seven'])
# print(df)
zd={'one':{'a':1,'b':2},
    'two':{'a':4,'c':5},
    'three':{'a':5,'d':6}}
data1 = pd.DataFrame(zd)
# print(data1)















