# # 理解高斯核函数
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.arange(-4,5,1)
# y = np.array((x>=-2)&(x<=2),dtype='int')
# plt.scatter(x[y==0],[0]*len(x[y==0]))
# plt.scatter(x[y==1],[0]*len(x[y==1]))
# plt.show()
#
# def gaussian(x, l):
#     gamma = 1.0
#     # 高斯核函数公式
#     return np.exp(-gamma * (x-l)**2)
#
# l1, l2 = -1 ,1
#
# X_new = np.empty((len(x),2))
# for i , data in enumerate(x):
#     X_new[i,0] = gaussian(data,l1)
#     X_new[i,1] = gaussian(data,l2)
#
# plt.scatter(X_new[y==0,0],X_new[y==0,1])
# plt.scatter(X_new[y==1,0],X_new[y==1,1])
# plt.show()
#

# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn import datasets
#
# X, y = datasets.make_moons(noise=0.15,random_state=666)
# from sklearn.preprocessing import StandardScaler
# from sklearn.svm import SVC
# from sklearn.pipeline import Pipeline
#
# def RBFKernelSVC( gamma=1.0):
#     return Pipeline([
#
#         ('std_scaler', StandardScaler()),
#         ('linearSVC', SVC(kernel='rbf', gamma=gamma))# gamma越 高，越 过拟合
#     ])
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
# svc = RBFKernelSVC(gamma=1)
# svc.fit(X,y)
#
# plot_decision_boundary(svc, axis=[-1.5, 2.5, -1.0, 1.5])
# plt.scatter(X[y==0,0], X[y==0,1])
# plt.scatter(X[y==1,0], X[y==1,1])
# plt.show()

#SVM解决回归问题
# margin范围中点越多越好
import numpy as np
import matplotlib.pyplot as plt
from  sklearn import  datasets
boston = datasets.load_boston()
X= boston.data
y = boston.target

from  sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,random_state=666)

from sklearn.svm import LinearSVR
from  sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

def StanderLinearSVR(epsilon=0.1):
    return Pipeline([
        ('std_scaler',StandardScaler()),
        ('linearSVR',LinearSVR(epsilon=epsilon))
    ])
svr = StanderLinearSVR()
svr.fit(X_train,y_train)
print(svr.score(X_test,y_test)) # 0.635951265133071







