import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
f=open('bike.csv')
data=pd.read_csv(f)
data=data[data['StartDay']==data['EndDay']]
data=data[['MemberType', 'TripDurationSec', 'BikeID', 'StartDay', 'StartDateTime',
       'StartDate', 'StartTime', 'StartStationName', 'StartStationID',
       'EndDay', 'EndDateTime', 'EndDate', 'EndTime', 'EndStationName',
       'EndStationID']]

data=data.dropna(how='all')
data['StartTime']=data.StartTime.map(lambda x:x.split(':')[0])
data['StartDate']=data.StartDate.map(lambda x:x.split('/')[0])
table = data.pivot_table(values='TripDurationSec',index='StartDay',
                         columns='MemberType',aggfunc=np.mean)
# print(table)
# table.plot.bar(stacked=True,rot=30)
table_norm=table.div(table.sum(axis=1),axis=0)#每个元素的比例值
# table_norm.plot.bar(stacked=True)
table2=data.pivot_table(values='TripDurationSec',index='StartTime',columns='MemberType',
                        aggfunc=np.mean)
# table2.plot.bar(rot=0)
shuliang=data.StartStationName.value_counts()-data.EndStationName.value_counts()
# print(shuliang.sort_values())
table=data.pivot_table(values='StartTime',index='StartStationName',columns=['MemberType','StartDay'],
                       aggfunc=np.size,margins=True,fill_value=0)
print(table['Customer'])









plt.show()