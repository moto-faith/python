# #支撑向量机 SVM
# import numpy as np
# import matplotlib.pyplot as plt
#
# from sklearn import datasets
# iris = datasets.load_iris()
#
# X = iris.data
# y= iris.target
#
# # 使用两个分类，两个特征
# X=X[y<2,:2]
# y = y[y<2]
#
# plt.scatter(X[y==0,0],X[y==0,1],color = 'r')
# plt.scatter(X[y==1,0],X[y==1,1],color = 'b')
# plt.show()
#
# # 数据归一化
# from sklearn.preprocessing import StandardScaler
# standardScaler = StandardScaler()
# standardScaler.fit(X)
# X_standard = standardScaler.transform(X)
#
# from sklearn.svm import LinearSVC
# svc = LinearSVC(C=1e9)
# svc.fit(X_standard,y)
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
# plot_decision_boundary(svc, axis=[-3, 3, -3, 3])
# plt.scatter(X_standard[y==0,0],X_standard[y==0,1],color = 'r')
# plt.scatter(X_standard[y==1,0],X_standard[y==1,1],color = 'b')
# plt.show()
#
# svc2 = LinearSVC(C=0.01)
# svc2.fit(X_standard,y)
#
# plot_decision_boundary(svc2, axis=[-3, 3, -3, 3])
# plt.scatter(X_standard[y==0,0],X_standard[y==0,1],color = 'r')
# plt.scatter(X_standard[y==1,0],X_standard[y==1,1],color = 'b')
# plt.show()
#
#
# def plot_svc_decision_boundary(model, axis):
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
#     w = model.coef_[0]
#     b = model.intercept_[0]
#
#     # w0*x0 + w1*x1 + b = 0
#     # => x1 = -w0/w1 * x0 - b/w1
#     plot_x = np.linspace(axis[0], axis[1], 200)
#     up_y = -w[0] / w[1] * plot_x - b / w[1] + 1 / w[1]# 边界上面的线
#     down_y = -w[0] / w[1] * plot_x - b / w[1] - 1 / w[1]# 边界下面的线
#
#     up_index = (up_y >= axis[2]) & (up_y <= axis[3])
#     down_index = (down_y >= axis[2]) & (down_y <= axis[3])
#     plt.plot(plot_x[up_index], up_y[up_index], color='black')
#     plt.plot(plot_x[down_index], down_y[down_index], color='black')
#
# plot_svc_decision_boundary(svc, axis=[-3, 3, -3, 3])
# plt.scatter(X_standard[y==0,0], X_standard[y==0,1])
# plt.scatter(X_standard[y==1,0], X_standard[y==1,1])
# plt.show()
#
# plot_svc_decision_boundary(svc2, axis=[-3, 3, -3, 3])
# plt.scatter(X_standard[y==0,0], X_standard[y==0,1])
# plt.scatter(X_standard[y==1,0], X_standard[y==1,1])
# plt.show()


# SVM 中使用多项式特征
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets

X, y = datasets.make_moons(noise=0.15,random_state=666)
plt.scatter(X[y==0,0],X[y==0,1])
plt.scatter(X[y==1,0],X[y==1,1])
plt.show()

from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.svm import LinearSVC
from sklearn.pipeline import Pipeline

def PolynomiaSVC(degree, C=1.0):
    return Pipeline([
        ('poly', PolynomialFeatures(degree=degree)),
        ('std_scaler', StandardScaler()),
        ('linearSVC', LinearSVC(C=C))
    ])

poly_svc =PolynomiaSVC(degree=3)
poly_svc.fit(X,y)

def plot_decision_boundary(model, axis):
    x0, x1 = np.meshgrid(
        np.linspace(axis[0], axis[1], int((axis[1] - axis[0]) * 100)).reshape(-1, 1),
        np.linspace(axis[2], axis[3], int((axis[3] - axis[2]) * 100)).reshape(-1, 1),
    )
    X_new = np.c_[x0.ravel(), x1.ravel()]

    y_predict = model.predict(X_new)
    zz = y_predict.reshape(x0.shape)

    from matplotlib.colors import ListedColormap
    custom_cmap = ListedColormap(['#EF9A9A', '#FFF59D', '#90CAF9'])

    plt.contourf(x0, x1, zz, linewidth=5, cmap=custom_cmap)

plot_decision_boundary(poly_svc, axis=[-1.5, 2.5, -1.0, 1.5])
plt.scatter(X[y==0,0],X[y==0,1],color = 'r')
plt.scatter(X[y==1,0],X[y==1,1],color = 'b')
plt.show()

# 多项式核函数的SVM
from sklearn.svm import SVC

def PolynomialKernelSVC(degree, C=1.0):
    return Pipeline([
        ('std_scaler', StandardScaler()),
        ('kernelSVC', SVC(kernel='poly', degree=degree, C=C))# kernel = 'poly'决定了是多项式
    ])

poly_kenel_svc = PolynomialKernelSVC(degree=3)
poly_kenel_svc.fit(X,y)
plot_decision_boundary(poly_kenel_svc, axis=[-1.5, 2.5, -1.0, 1.5])
plt.scatter(X[y==0,0],X[y==0,1],color = 'r')
plt.scatter(X[y==1,0],X[y==1,1],color = 'b')
plt.show()
