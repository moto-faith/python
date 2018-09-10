import numpy as np
import matplotlib.pyplot as plt
from SimpleLinearRegression import SimpleLinearRegression
import time
from sklearn import datasets

# x=np.array([i for i in range(1,6)],dtype=float)
# y=np.array([1,3,2,3,5],dtype=float)

# plt.scatter(x,y)
# plt.axis([0,6,0,6])
# plt.show()
# x_mean = np.mean(x)
# y_mean = np.mean(y)
# num=0.0#num 为a 推导式中的分子部分
# d=0.0#d 为a 推导式中分母部分
#
# for x_i , y_i in zip(x,y):
#     num+=(x_i-x_mean)*(y_i-y_mean)
#     d+=(x_i-x_mean)**2
# a=num/d#回归方程式中的a 已求得
# b=y_mean-a*x_mean#回归方程式中的b 已求得
#
# y_hat=a*x+b #线性回归方程式
#
# plt.scatter(x,y) #原数据中的各个数据
# plt.plot(x,y_hat,color='r') #回归方程的线,红色
# plt.axis([0,6,0,6])
# plt.show()
#
# x_predict = 6  #待预测的数据
# y_predict = a*x_predict+b #套用公式得到预测结果
# print(y_predict) #5.2

# x_predict=np.array([6])
# regal = SimpleLinearRegression1()
# regal.fit(x,y)
# y_predict = regal.predict(x_predict)
# print(y_predict) #[5.2]
# print(regal.a_) #0.8 回归方程的a参数
# print(regal.b_)  #0.39999999999999947 回归方程的b参数

# time1=time.time()
# m=1000000
# big_x = np.random.random(m)
# big_y = big_x*2+3+np.random.normal(size=m) #对big_x进行修改得到相应的y
#
# # x_predict=np.array([6])
#
# regal = SimpleLinearRegression()
# regal.fit(big_x,big_y)
#
# time2=time.time()
# print(time2-time1) # 2方法耗时=0.12771224975585938  1方法耗时=1.052039384841919

# y_predict = regal.predict(x_predict)
# print(y_predict) #[5.2]
# print(regal.a_) #0.8 回归方程的a参数
# print(regal.b_)  #0.39999999999999947 回归方程的b参数

boston = datasets.load_boston()#使用波士顿房价数据
# print(boston.keys()) #dict_keys(['data', 'target', 'feature_names', 'DESCR', 'filename'])
# print(boston.feature_names) #['CRIM' 'ZN' 'INDUS' 'CHAS' 'NOX' 'RM' 'AGE' 'DIS' 'RAD' 'TAX' 'PTRATIO' 'B' 'LSTAT']
x=boston.data[:,5]#房间数量
# print(x.shape)
y=boston.target #总房价 单位（万）
# plt.scatter(x,y)
# plt.show()#由图可看出50就是边界，有一些值在边界干扰了整体数据，需要清除

x=x[y<50]
y=y[y<50]
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y,random_state=666)#把总数据分出训练集和测试集
reg = SimpleLinearRegression()
reg.fit(x_train,y_train)
y_predict= reg.predict(x_test)
# plt.scatter(x_test,y_test)
# plt.scatter(x_test,reg.predict(x_test))
# plt.show()

# #MSE
# mse_test = np.sum((y_predict - y_test)**2) / len(y_test)
#
# #RMSE
# from math import sqrt
# rmse_test = sqrt(mse_test)
#
# #MAE
# mae_test = np.sum(np.absolute(y_predict - y_test))/len(y_test)
#
# print(mse_test)#36.01765800113341
# print(rmse_test)#6.00147131969598
# print(mae_test)#4.269939110386622

# #使用自己写的包
# from metrics import mean_absolute_error
# from metrics import root_mean_squared_error
# from metrics import mean_squared_error
#
# MSE = mean_squared_error(y_test,y_predict)
# RMSE = root_mean_squared_error(y_test,y_predict)
# MAE = mean_absolute_error(y_test,y_predict)
# print(MSE)#30.383242067794136
# print(RMSE)#5.512099606120533
# print(MAE)#3.9974445446147038

#使用sklearn自带的MES和MAE（自带的没有RMSE）
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from math import sqrt
mae = mean_absolute_error(y_test,y_predict)
mse = mean_squared_error(y_test,y_predict)
rmse = sqrt(mse)
# print(mse)#29.21058810116948
# print(rmse)#5.404682053661388
# print(mae)#3.8319110253303648

RS = 1-mean_squared_error(y_test,y_predict)/np.var(y_test)
print(RS) #0.5682464825049474


from metrics import r2_score#用自己写入的包
RS = r2_score(y_test,y_predict)
print(RS) #0.5682464825049474

from sklearn.metrics import r2_score #用sklearn中自带的RS方法
RS = r2_score(y_test,y_predict)
print(RS) #0.5682464825049474

RS = reg.score(x_test,y_test) #用写入SimpleLinearRegression的方法
print(RS) #0.5682464825049474
