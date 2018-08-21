import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_list=[]
for i in range(1,8):
    try:
        f=open('lianjia{}.csv'.format(i),encoding='gbk')
        data=pd.read_csv(f)
    except:
        f = open('lianjia{}.csv'.format(i),encoding='utf-8')
        data=pd.read_csv(f)
    data_list.append(data)
data=pd.concat(data_list)#把7个表连接成一个
# print(data.info())查看连接是否成功
# print(data.columns)
data=data[['cjdanjia','cjxiaoqu','cjlouceng','bankuai','xingming','cjzongjia','congyenianxian','cjshijian', 'mendian',  'zhiwei']]
# print((data.isnull()).sum())#查看每项缺失的数量
# print(data[data.cjdanjia.isnull()])#找到缺失的那项，发现是无效条目
data=data.dropna(how='all')#删去那个无效条目
# print(data.isnull().sum())
# print(data.duplicated().sum())#查看重复条目数量
# print(data.duplicated(subset=['cjdanjia','cjxiaoqu','cjlouceng','bankuai']).sum())
data.sort_values(by='bankuai',inplace=True)#按bankuai排列,把bankuai为空的放在后面
data.drop_duplicates(subset=['cjdanjia','cjxiaoqu','cjlouceng'],inplace=True)
#去掉了完全null的条目，去掉了重复的条目

data.cjdanjia=data.cjdanjia.str.replace('元/平','').astype(np.float32).map(lambda x:round(x/10000,2))
#去掉'元/平',把单价转化为float类型,把数字除以10000并保留两位小数
data=data[data.cjdanjia>0.5]#单价小于5000一平为不正常数据,筛选正常数据

bins=[0,1,2,3,4,5,7,9,11,13,15]
# print((pd.cut(data.cjdanjia,bins)).value_counts())#以bins为区间分段,看在各区间的数量
# (pd.cut(data.cjdanjia,bins)).value_counts().plot.bar(rot=30)
# plt.show()

data['chaoxiang']=data.cjlouceng.map(lambda x:x.split('/')[0])
data['louceng']=data.cjlouceng.map(lambda x:x.split('/')[1])#把朝向和楼层分隔出来
# print(data.louceng.unique())#发现楼层有'未知'和空
data=data[(data.louceng!='未知') & (data.louceng!='')]
data.join(pd.get_dummies(data.louceng))
# print(pd.get_dummies(data.louceng).sum())
# pd.get_dummies(data.louceng).sum().plot.bar(rot=30)
# plt.show()#把各种楼层求和并画图
# pd.get_dummies(data.louceng).sum().to_csv('loucengbu.csv',encoding='utf-8')#保存各楼层和为csv

data['cjshijian']=data.cjshijian.map(lambda x:x.split('：')[1])
data['year']=data.cjshijian.map(lambda x:x.split('-')[0])
# print(data.groupby(['year','xingming'])['xingming'].count())各个销售员的销售数量
# print(data.groupby(['year','mendian'])['mendian'].count()) 各个门店的销售情况
data_group=data.groupby(['xingming','congyenianxian'])['cjzongjia'].sum()
# print(data_group[data_group>10000])销售额大于1亿的销售人员
data_1w=data.pivot_table('cjzongjia',index='xingming',columns='congyenianxian',aggfunc=sum)
# print((data_1w>10000).sum())










