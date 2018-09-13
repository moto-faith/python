# #随机梯度下降法
# import numpy as np
# import matplotlib.pyplot as plt
# from LinearRegression import LinearRegression
# import time
#
# m = 100000
# x= np.random.normal(size=m)
# X = x.reshape(-1,1) #十万个样本，1个特征值
# y= 4. *x + 3. + np.random.normal(0,3,size=m)#生成对应的y
# # plt.scatter(x,y)
# # plt.show()
#
# #下降梯度法
# time1 = time.time()
# reg = LinearRegression()
# reg.fit_gd(X,y)
# time2 = time.time()
# print(reg.intercept_) #截距2.990569149132685
# print(reg.coef_) #斜率 [4.00122884]
# print(time2-time1) #用时 3.2365267276763916
#
#
# #随机下降梯度法
# def dJ_sgd(theta, X_b_i, y_i):
#     return 2 * X_b_i.T.dot(X_b_i.dot(theta) - y_i) #计算单个样本的学习率
#
# def sgd(X_b, y, initial_theta, n_iters):
#
#     t0, t1 = 5, 50
#     def learning_rate(t):
#         return t0 / (t + t1)#为了使学习率每次变化不会太大而设置，例如不会从1/1 -> 1/2那样变化过大
#
#     theta = initial_theta
#     for cur_iter in range(n_iters):
#         rand_i = np.random.randint(len(X_b))#随机一个索引
#         gradient = dJ_sgd(theta, X_b[rand_i], y[rand_i])
#         theta = theta - learning_rate(cur_iter) * gradient #计算出下一个theta,直到循环结束
#
#     return theta
#
# time3 = time.time()
# X_b = np.hstack([np.ones((len(X), 1)), X])
# initial_theta = np.zeros(X_b.shape[1]) #初始化的theta值
# theta = sgd(X_b, y, initial_theta, n_iters=m//3) #不再设置小于精度停止，而循环1/3个样本数量就停止
# time4 = time.time()
# print(theta) #[3.00473864 4.03888856]
# print(time4-time3) #用时0.2941594123840332

# import numpy as np
# import matplotlib.pyplot as plt
# from LinearRegression import LinearRegression
# import time
#
# m = 100000
# x= np.random.normal(size=m)
# X = x.reshape(-1,1) #十万个样本，1个特征值
# y= 4. *x + 3. + np.random.normal(0,3,size=m)#生成对应的y
#
# #封装的梯度下降法
# lin_reg = LinearRegression()
# lin_reg.fit_bgd(X, y)
# print(lin_reg.intercept_, lin_reg.coef_) #2.994310433411695 [4.00844721]
#
# #封装的随机梯度下降法
# lin_reg = LinearRegression()
# lin_reg.fit_sgd(X, y, n_iters=2)
# print(lin_reg.intercept_, lin_reg.coef_) #2.994488600701022 [4.00927082]

# from sklearn import datasets
#
# boston = datasets.load_boston()
# X = boston.data
# y = boston.target
#
# X = X[y < 50.0]
# y = y[y < 50.0]
#
# from model_selection import train_test_split
#
# X_train, X_test, y_train, y_test = train_test_split(X, y, seed=666)
#
# from sklearn.preprocessing import StandardScaler
#
# standardScaler = StandardScaler()
# standardScaler.fit(X_train)
# X_train_standard = standardScaler.transform(X_train)
# X_test_standard = standardScaler.transform(X_test)
#
# from LinearRegression import LinearRegression
# #循环整个数据的次数越多，准确度越高
# lin_reg = LinearRegression()
# lin_reg.fit_sgd(X_train_standard, y_train, n_iters=2)#0.7857275413602651
# print(lin_reg.score(X_test_standard, y_test))
# lin_reg.fit_sgd(X_train_standard, y_train, n_iters=50)#0.8085607570556209
# print(lin_reg.score(X_test_standard, y_test))
# lin_reg.fit_sgd(X_train_standard, y_train, n_iters=100)#0.8129434245278827
# print(lin_reg.score(X_test_standard, y_test))
#
# from sklearn.linear_model import SGDRegressor
#
# sgd_reg = SGDRegressor(max_iter=50)
# sgd_reg.fit(X_train_standard,y_train)
# print(sgd_reg.score(X_test_standard,y_test)) #0.8124610674601445

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(666)
X= np.random.random(size=(1000,10)) # 设置1000个样本，10个特征的数据

true_theta = np.arange(1,12,dtype=float)
X_b = np.hstack([np.ones((len(X),1)),X])
y=X_b.dot(true_theta)+np.random.normal(size=1000)

def J(theta, X_b, y):
    try:
        return np.sum((y - X_b.dot(theta))**2) / len(X_b)
    except:
        return float('inf')

def dJ_math(theta, X_b, y):
    return X_b.T.dot(X_b.dot(theta) - y) * 2. / len(y)

def dJ_debug(theta, X_b, y, epsilon=0.01):
    res = np.empty(len(theta))
    for i in range(len(theta)):
        theta_1 = theta.copy()
        theta_1[i] += epsilon
        theta_2 = theta.copy()
        theta_2[i] -= epsilon
        res[i] = (J(theta_1, X_b, y) - J(theta_2, X_b, y)) / (2 * epsilon)
    return res


def gradient_descent(dJ, X_b, y, initial_theta, eta, n_iters=1e4, epsilon=1e-8):
    theta = initial_theta
    cur_iter = 0

    while cur_iter < n_iters:
        gradient = dJ(theta, X_b, y)
        last_theta = theta
        theta = theta - eta * gradient
        if (abs(J(theta, X_b, y) - J(last_theta, X_b, y)) < epsilon):
            break

        cur_iter += 1

    return theta

X_b = np.hstack([np.ones((len(X), 1)), X])
initial_theta = np.zeros(X_b.shape[1])
eta = 0.01

theta = gradient_descent(dJ_debug, X_b, y, initial_theta, eta) #使用两点间求斜率得出的theta
print(theta) #[ 1.1251597   2.05312521  2.91522497  4.11895968  5.05002117  5.90494046 6.97383745  8.00088367  8.86213468  9.98608331 10.90529198]

theta = gradient_descent(dJ_math, X_b, y, initial_theta, eta)#使用公式得出的theta
print(theta) #[ 1.1251597   2.05312521  2.91522497  4.11895968  5.05002117  5.90494046 6.97383745  8.00088367  8.86213468  9.98608331 10.90529198]




