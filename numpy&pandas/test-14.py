import pandas as pd
f=open(r'C:\Users\10640\python\ips.csv')
data = pd.read_csv(f,sep='\t',header=None,names={'one','two','three','four','five','six'})
# print(data)
# data.to_csv('abc.csv')











