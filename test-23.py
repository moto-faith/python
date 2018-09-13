#梯度下降法 波士顿房价
# # import numpy as np
# # import matplotlib.pyplot as plt
# #
# # plot_x = np.linspace(-1,6,141) #从-1到6等差取141个数字
# # plot_y = (plot_x-2.5)**2-1 #对x进行加工得到y
# # # plt.plot(plot_x,plot_y)
# # # plt.show()
# # theta_history = []
# #
# # def J(theta):
# #     try:
# #         return (theta-2.5)**2 - 1.
# #     except:
# #         return float('inf')
# #
# # def dJ(theta):
# #     return 2*(theta-2.5)
# #
# # def gradient_descent(initial_theta, eta,n_iter = 1e4, epsilon=1e-8):
# #     theta = initial_theta
# #     i_iter = 0
# #     theta_history.append(initial_theta)
# #
# #     while i_iter<n_iter:
# #         gradient = dJ(theta)
# #         last_theta = theta
# #         theta = theta - eta * gradient
# #         theta_history.append(theta)
# #
# #         if (abs(J(theta) - J(last_theta)) < epsilon):
# #             break
# #         i_iter+=1
# #
# # def plot_theta_history():
# #     plt.plot(plot_x, J(plot_x))
# #     plt.plot(np.array(theta_history), J(np.array(theta_history)), color="r", marker='+')
# #     plt.show()
# #
# # eta = 1.1
# # theta_history = []
# # gradient_descent(0,eta,n_iter=10)
# # plot_theta_history()
# #
# #
#
#
# import numpy as np
# import matplotlib.pyplot as plt
# np.random.seed(666)
# x=2*np.random.normal(size=100)# 设置100个均值为0 方差为1 的正态分布数
# X=x.reshape(-1,1) #相当于一个特征值  有100个样本
# y=x*3. + 4. + np.random.normal(size=100) #把每个x乘3 加4再加以噪音（斜率3，截距4）
#
# # plt.scatter(x,y)
# # plt.show()
#
# def J(theta,X_b,y):
#     try:
#         return np.sum((y-X_b.dot(theta))**2)/len(X_b) #返回的是MSE，错误率
#     except:
#         return float('inf')
#
# def dJ(theta,X_b,y):
#     res = np.empty(len(theta))
#     res[0]=np.sum(X_b.dot(theta)-y) #对theta0的求导
#     for i in range(1,len(theta)): #对剩下的theta求导
#         res[i] = (X_b.dot(theta)-y).dot(X_b[:,i])
#     return res*2/len(X_b) #返回每次移动的△J
#
#
# def gradient_descent(X_b, y, initial_theta, eta, n_iters=1e4, epsilon=1e-8):
#     theta = initial_theta
#     cur_iter = 0
#
#     while cur_iter < n_iters: #设置最多找10000个点
#         gradient = dJ(theta, X_b, y) #得到每次移动的△J
#         last_theta = theta
#         theta = theta - eta * gradient #下一个点的位置
#         if (abs(J(theta, X_b, y) - J(last_theta, X_b, y)) < epsilon): #如果临近的两次错误率的差小于精度就找到了最小错误率
#             break
#
#         cur_iter += 1
#
#     return theta
#
# X_b = np.hstack([np.ones((len(x),1)),X])
# initial_theta = np.zeros(X_b.shape[1])#存放截距和各个特征值的系数
#
# eta = 0.01
# theta = gradient_descent(X_b,y,initial_theta,eta)
# print(theta) #第一个值是截距，之后每项为各个特征值的系数  [4.04395392 3.04269392]
#
#
# from LinearRegression import LinearRegression
# reg = LinearRegression()
# reg.fit_gd(X,y)
# print(reg.intercept_) #输出theta0
# print(reg.coef_) #输出每个系数
#
# import numpy as np
# from sklearn import datasets
# boston = datasets.load_boston()
# X=boston.data
# y=boston.target
#
# X=X[y<50.0]
# y=y[y<50.0]
#
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=666)
#
#
# #使用线性回归
# from LinearRegression import LinearRegression
# reg1 = LinearRegression()
# reg1.fit_normal(X_train,y_train)
# score1 = reg1.score(X_test,y_test)
# print(score1) #0.8009390227581148
#
# #使用梯度下降法
# reg2 = LinearRegression()
# reg2.fit_gd(X_train,y_train,eta=0.000001,n_iters=1e6) #需要将eta的值设置的小一点，因为有的特征数值很大
# print(reg2.score(X_test,y_test)) #0.737942001474466
# #因为没有把数值归一化，所以，每一次用eta时，对每个特征值的改变差距很大，耗时比较久,结果也不准确
#
# #先把数据归一化再训练模型
# from sklearn.preprocessing import StandardScaler
# standardScaler = StandardScaler()
# standardScaler.fit(X_train)
# X_train_standardScaler = standardScaler.transform(X_train)
# reg3 = LinearRegression()
# reg3.fit_gd(X_train_standardScaler,y_train)
# X_test_standardScaler = standardScaler.transform(X_test)
# score3 = reg3.score(X_test_standardScaler,y_test)
# print(score3) #0.8009270105386639 结果正常了


# import numpy as np
# from LinearRegression import LinearRegression
# import time
# m = 1000 #样本数量
# n = 5000 #特征值数量
#
# big_X = np.random.normal(size=(m, n))
#
# true_theta = np.random.uniform(0.0, 100.0, size=n+1)#设置theta值
#
# big_y = big_X.dot(true_theta[1:]) + true_theta[0] + np.random.normal(0., 10., size=m) #用设置的theta值得到y
#
# #线性回归法
# time1= time.time()
# big_reg1 = LinearRegression()
# big_reg1.fit_normal(big_X,big_y)
# time2 = time.time()
# print(time2-time1)#训练模型所用的时间
#
# #梯度下降法
# time3 = time.time()
# big_reg2 = LinearRegression()
# big_reg2.fit_gd(big_X,big_y)
# time4 = time.time()
# print(time4-time3)#训练模型所用的时间




