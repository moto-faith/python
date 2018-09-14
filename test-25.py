# #主成分分析法
# import numpy as np
# import matplotlib.pyplot as plt
#
# #生成样本
# X = np.empty((100,2))#100个样本 2个特征
# X[:,0] = np.random.uniform(0.,100.,size=100)
# X[:,1] = 0.75 * X[:,0] + 3. +np.random.normal(0,10, size=100)
# # plt.scatter(X[:,0],X[:,1])
# # plt.show()
#
# #均值归0
# def demean(X):
#     return X-np.mean(X,axis=0)
# X_demean = demean(X)
# # plt.scatter(X_demean[:,0],X_demean[:,1])
# # plt.show()
#
# #上升梯度法
# def f(w,X):#方差值
#     return np.sum((X.dot(w))**2)/len(X)
#
# def df_math(w,X):#方差倒数，即斜率
#     return X.T.dot(X.dot(w))* 2./len(X)
#
# def df_debug(w,X,epsilon=0.0001):#原始方法验证w是否正确
#     res = np.empty(len(w))
#     for i in range(len(w)):
#         w_1 = w.copy()
#         w_1[i]+=epsilon
#         w_2 = w.copy()
#         w_2[i]-=epsilon
#         res[i]=(f(w_1,X)-f(w_2,X)) / (2*epsilon)
#     return res
#
# def direction(w):# w 转换为单位向量，只要方向即可
#     return w / np.linalg.norm(w)
#
# def gradient_ascent(df,X,initial_w,eta,n_iters = 1e4,epsilon = 1e-8):#上升梯度法
#     w = direction(initial_w)#把初始化的w 转为单位向量
#     cur_iter = 0#目前循环次数
#     while cur_iter < n_iters:
#         gradient = df(w,X)
#         last_w = w
#         w= w + eta * gradient #每次上升不同高度，斜率越靠近0，上升高度越小
#         w = direction(w) # 注意1：每次求一个单位方向
#         if(abs(f(w,X)-f(w,last_w))<epsilon):
#             break
#         cur_iter+=1
#     return w
#
# initial_w = np.random.random(X.shape[1]) ## 注意2：初始化的 w 不能用0向量开始
# eta = 0.001
# # 注意3： 不能使用StandardScaler标准化数据
#
# w = gradient_ascent(df_debug,X_demean,initial_w,eta)
# print(w)#[0.78660631 0.61745487]
#
# w = gradient_ascent(df_math,X_demean,initial_w,eta)
# print(w)#[0.78660631 0.61745487]
#
# plt.scatter(X_demean[:,0],X_demean[:,1])
# plt.plot([0,w[0]*100],[0,w[1]*100],color = 'r')
# plt.show()

#获得前n个主成分
import numpy as np
import matplotlib.pyplot as plt
X = np.empty((100, 2))
X[:,0] = np.random.uniform(0., 100., size=100)
X[:,1] = 0.75 * X[:,0] + 3. + np.random.normal(0, 10., size=100)

def demean(X):
    return X - np.mean(X, axis=0)
X = demean(X)


def f(w, X):
    return np.sum((X.dot(w) ** 2)) / len(X)


def df(w, X):
    return X.T.dot(X.dot(w)) * 2. / len(X)


def direction(w):
    return w / np.linalg.norm(w)


def first_component(X, initial_w, eta, n_iters=1e4, epsilon=1e-8):
    w = direction(initial_w)
    cur_iter = 0

    while cur_iter < n_iters:
        gradient = df(w, X)
        last_w = w
        w = w + eta * gradient
        w = direction(w)
        if (abs(f(w, X) - f(last_w, X)) < epsilon):
            break

        cur_iter += 1

    return w

initial_w = np.random.random(X.shape[1])
eta = 0.01
w = first_component(X, initial_w, eta)# 第一主成分的单位向量

X2 = X - X.dot(w).reshape(-1, 1) * w # X 在第二主成分中的映射

w2 = first_component(X2, initial_w, eta) #第二主成分的单位向量

print(w.dot(w2))#两垂直向量相乘 2.387548196425282e-06

#求特征值在多主城分中的单位向量
def first_n_components(n, X, eta=0.01, n_iters=1e4, epsilon=1e-8):
    X_pca = X.copy()
    X_pca = demean(X_pca)
    res = []
    for i in range(n):
        initial_w = np.random.random(X_pca.shape[1])
        w = first_component(X_pca, initial_w, eta)
        res.append(w)

        X_pca = X_pca - X_pca.dot(w).reshape(-1, 1) * w

    return res

w= first_n_components(2, X)
print(w) #[array([0.77252383, 0.63498578]), array([-0.63498371,  0.77252553])]