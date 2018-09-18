#决策树

# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn import datasets
#
# iris = datasets.load_iris()
# X = iris.data[:,2:]
# y = iris.target
# plt.scatter(X[y==0,0],X[y==0,1],color = 'blue')
# plt.scatter(X[y==1,0],X[y==1,1],color='red')
# plt.scatter(X[y==2,0],X[y==2,1],color='green')
# plt.show()
#
# #使用sklearn中的决策树
# from sklearn.tree import DecisionTreeClassifier
# dt_clf = DecisionTreeClassifier(max_depth=2,criterion='entropy',random_state=42)
# dt_clf.fit(X,y)
#
# #画出决策边界
# def plot_decision_boundary(model, axis):
#     x0, x1 = np.meshgrid(
#         np.linspace(axis[0], axis[1], int((axis[1] - axis[0]) * 100)).reshape(-1, 1),
#         np.linspace(axis[2], axis[3], int((axis[3] - axis[2]) * 100)).reshape(-1, 1),
#     )
#     X_new = np.c_[x0.ravel(), x1.ravel()]
#
#     y_predict = model.predict(X_new)
#     zz = y_predict.reshape(x0.shape)
#
#     from matplotlib.colors import ListedColormap
#     custom_cmap = ListedColormap(['#EF9A9A', '#FFF59D', '#90CAF9'])
#
#     plt.contourf(x0, x1, zz, cmap=custom_cmap)
#
# plot_decision_boundary(dt_clf,axis=[0.5,7.5,0,3])
# plt.scatter(X[y==0,0],X[y==0,1],color = 'blue')
# plt.scatter(X[y==1,0],X[y==1,1],color='red')
# plt.scatter(X[y==2,0],X[y==2,1],color='green')
# plt.show()

#信息熵
# import numpy as np
# import matplotlib.pyplot as plt
# def entropy(p):
#     return -p * np.log(p) - (1-p) *np.log(1-p)
# x = np.linspace(0.01,0.99,200)
# plt.plot(x,entropy(x))
# plt.show()

# #使用信息熵寻找最优划分
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn import datasets
#
# iris = datasets.load_iris()
# X = iris.data[:,2:]
# y = iris.target
# plt.scatter(X[y==0,0],X[y==0,1],color = 'blue')
# plt.scatter(X[y==1,0],X[y==1,1],color='red')
# plt.scatter(X[y==2,0],X[y==2,1],color='green')
# plt.show()
#
#
#
# def spilt(X, y, d, value):
#     index_a = (X[:,d]<=value)
#     index_b = (X[:,d]>value)
#     return X[index_a], X[index_b], y[index_a], y[index_b]
#
# from collections import Counter
# from math import log
# def entropy(y):
#     counter = Counter(y)
#     res = 0.0
#     for num in counter.values():
#         p = num /len(y)
#         res+= -p *log(p)
#     return  res
#
# def try_split(X, y):
#     best_entropy = float('inf')
#     best_d, best_v = -1, -1
#     for d in range(X.shape[1]):
#         sort_index = np.argsort(X[:,d])
#         for i in range(1,len(X)):
#             if X[sort_index[i],d] != X[sort_index[i-1],d]:
#                 v = (X[sort_index[i-1], d] + X[sort_index[i], d] )/ 2
#                 X_1, X_r, y_1, y_r = spilt(X, y, d, v)
#                 p_l, p_r = len(X_1) / len(X), len(X_r) / len(X)
#                 e = p_l *entropy(y_1) + p_r * entropy(y_r)
#                 if e < best_entropy:
#                     best_entropy, best_d, best_v = e, d, v
#
#     return best_entropy, best_d, best_v
#
# best_entropy, best_d, best_v = try_split(X, y)
# print("best_entropy =", best_entropy)
# print("best_d =", best_d)
# print("best_v =", best_v)
# X1_l, X1_r, y1_l, y1_r = spilt(X, y, best_d, best_v)
# best_entropy2, best_d2, best_v2 = try_split(X1_r, y1_r)
# print("best_entropy =", best_entropy2)
# print("best_d =", best_d2)
# print("best_v =", best_v2)
# # best_entropy = 0.46209812037329684
# # best_d = 0
# # best_v = 2.45
# # best_entropy = 0.2147644654371359
# # best_d = 1
# # best_v = 1.75

# 基尼系数选择最优划分
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn import datasets
#
# iris = datasets.load_iris()
# X = iris.data[:,2:]
# y = iris.target
#
# #使用sklearn中的决策树
# from sklearn.tree import DecisionTreeClassifier
# dt_clf = DecisionTreeClassifier(max_depth=2,criterion='gini',random_state=42)
# dt_clf.fit(X,y)
#
# #画出决策边界
# def plot_decision_boundary(model, axis):
#     x0, x1 = np.meshgrid(
#         np.linspace(axis[0], axis[1], int((axis[1] - axis[0]) * 100)).reshape(-1, 1),
#         np.linspace(axis[2], axis[3], int((axis[3] - axis[2]) * 100)).reshape(-1, 1),
#     )
#     X_new = np.c_[x0.ravel(), x1.ravel()]
#
#     y_predict = model.predict(X_new)
#     zz = y_predict.reshape(x0.shape)
#
#     from matplotlib.colors import ListedColormap
#     custom_cmap = ListedColormap(['#EF9A9A', '#FFF59D', '#90CAF9'])
#
#     plt.contourf(x0, x1, zz, cmap=custom_cmap)
#
# plot_decision_boundary(dt_clf,axis=[0.5,7.5,0,3])
# plt.scatter(X[y==0,0],X[y==0,1])
# plt.scatter(X[y==1,0],X[y==1,1])
# plt.scatter(X[y==2,0],X[y==2,1])
# plt.show()
#
# from collections import Counter
#
# def split(X, y, d, value):
#     index_a = (X[:, d] <= value)
#     index_b = (X[:, d] > value)
#     return X[index_a], X[index_b], y[index_a], y[index_b]
#
#
# def gini(y):
#     counter = Counter(y)
#     res = 1.0
#     for num in counter.values():
#         p = num / len(y)
#         res -= p ** 2
#     return res
#
#
# def try_split(X, y):
#     best_g = float('inf')
#     best_d, best_v = -1, -1
#     for d in range(X.shape[1]):
#         sorted_index = np.argsort(X[:, d])
#         for i in range(1, len(X)):
#             if X[sorted_index[i], d] != X[sorted_index[i - 1], d]:
#                 v = (X[sorted_index[i], d] + X[sorted_index[i - 1], d]) / 2
#                 X_l, X_r, y_l, y_r = split(X, y, d, v)
#                 p_l, p_r = len(X_l) / len(X), len(X_r) / len(X)
#                 g = p_l * gini(y_l) + p_r * gini(y_r)
#                 if g < best_g:
#                     best_g, best_d, best_v = g, d, v
#
#     return best_g, best_d, best_v
#
# best_g, best_d, best_v = try_split(X, y)
# print("best_g =", best_g)
# print("best_d =", best_d)
# print("best_v =", best_v)
# X1_l, X1_r, y1_l, y1_r = split(X, y, best_d, best_v)
# best_g2, best_d2, best_v2 = try_split(X1_r, y1_r)
# print("best_g =", best_g2)
# print("best_d =", best_d2)
# print("best_v =", best_v2)
# best_g = 0.3333333333333333
# # best_d = 0
# # best_v = 2.45
# # best_g = 0.1103059581320451
# # best_d = 1
# # best_v = 1.75

# CART
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn import datasets
#
# X, y = datasets.make_moons(noise=0.25, random_state=666)
#
# from sklearn.tree import DecisionTreeClassifier
#
# dt_clf = DecisionTreeClassifier(max_depth=3)
# dt_clf.fit(X, y)
#
#
# def plot_decision_boundary(model, axis):
#     x0, x1 = np.meshgrid(
#         np.linspace(axis[0], axis[1], int((axis[1] - axis[0]) * 100)).reshape(-1, 1),
#         np.linspace(axis[2], axis[3], int((axis[3] - axis[2]) * 100)).reshape(-1, 1),
#     )
#     X_new = np.c_[x0.ravel(), x1.ravel()]
#
#     y_predict = model.predict(X_new)
#     zz = y_predict.reshape(x0.shape)
#
#     from matplotlib.colors import ListedColormap
#     custom_cmap = ListedColormap(['#EF9A9A', '#FFF59D', '#90CAF9'])
#
#     plt.contourf(x0, x1, zz, linewidth=5, cmap=custom_cmap)
#
# plot_decision_boundary(dt_clf, axis=[-1.5, 2.5, -1.0, 1.5])
# plt.scatter(X[y==0,0], X[y==0,1])
# plt.scatter(X[y==1,0], X[y==1,1])
# plt.show()

#决策树的回归预测

# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn import datasets
#
# boston = datasets.load_boston()
# X = boston.data
# y = boston.target
#
# from sklearn.model_selection import train_test_split
#
# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=666)
#
# from sklearn.tree import DecisionTreeRegressor
#
# dt_reg = DecisionTreeRegressor()
# dt_reg.fit(X_train, y_train)
# print(dt_reg.score(X_test, y_test))# 0.6113530551173676
# print(dt_reg.score(X_train, y_train)) #1.0

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data[:,2:]
y = iris.target
from sklearn.tree import DecisionTreeClassifier

tree_clf = DecisionTreeClassifier(max_depth=2, criterion="entropy")
tree_clf.fit(X, y)


def plot_decision_boundary(model, axis):
    x0, x1 = np.meshgrid(
        np.linspace(axis[0], axis[1], int((axis[1] - axis[0]) * 200)).reshape(-1, 1),
        np.linspace(axis[2], axis[3], int((axis[3] - axis[2]) * 200)).reshape(-1, 1),
    )
    X_new = np.c_[x0.ravel(), x1.ravel()]

    y_predict = model.predict(X_new)
    zz = y_predict.reshape(x0.shape)

    from matplotlib.colors import ListedColormap
    custom_cmap = ListedColormap(['#EF9A9A', '#FFF59D', '#90CAF9'])

    plt.contourf(x0, x1, zz, linewidth=5, cmap=custom_cmap)
plot_decision_boundary(tree_clf, axis=[0.5, 7.5, 0, 3])
plt.scatter(X[y==0,0], X[y==0,1])
plt.scatter(X[y==1,0], X[y==1,1])
plt.scatter(X[y==2,0], X[y==2,1])
plt.show()

#删除一个样本的数据，重新分类
X_new = np.delete(X, 138, axis=0)
y_new = np.delete(y, 138)
tree_clf2 = DecisionTreeClassifier(max_depth=2, criterion="entropy")
tree_clf2.fit(X_new, y_new)
plot_decision_boundary(tree_clf2, axis=[0.5, 7.5, 0, 3])
plt.scatter(X[y==0,0], X[y==0,1])
plt.scatter(X[y==1,0], X[y==1,1])
plt.scatter(X[y==2,0], X[y==2,1])
plt.show()
