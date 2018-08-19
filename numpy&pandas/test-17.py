import pandas as pd
import numpy as np
df = pd.DataFrame({'animal':'cat dog cat fish dog cat cat'.split(),'size':list('SSMMMLL')
                   ,'adult':[False,False,False,False,False,True,True],'weight':[8,10,11,1,20,12,12]})
# print(df)
# print(df.groupby(df['animal'])['weight'].mean())
# print(df.groupby('animal')['weight'].mean())
# print(df.groupby('animal').mean())
# print(df.groupby(['animal','adult'])['weight'].mean())
data = df.groupby(np.array(['s','n','s','n','s','n','s']))['weight'].mean()
# print(data)
# print(df.groupby('animal').size())元素数量
df1 = df.set_index('animal')
# print(df1)
# print(df1.groupby(len)['weight'].mean())根据索引的字符长度进行分组
# print(df.groupby('animal')['weight'].apply(lambda x:x-x.mean()))
# print(df.groupby('animal').apply(lambda x:x['size'][x['weight'].idxmax()]))animal分组中最重的size
gb=df.groupby('animal')
# print(gb.get_group('cat'))




