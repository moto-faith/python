# import numpy as np
# import matplotlib.pyplot as plt
#
# def sigmoid(t):
#     return 1./(1.+np.exp(-t))
# x=np.linspace(-10,10,500)
# plt.plot(x,sigmoid(x))
# plt.show()

#鸢尾花逻辑分类
import  numpy as np
import matplotlib.pyplot as plt
from  sklearn import datasets

iris = datasets.load_iris()
X=iris.data
y=iris.target

X = X[y<2,:2]
y = y[y<2]

from model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, seed=666)

from LogisticRegression import LogisticRegression
log_reg = LogisticRegression()
log_reg.fit(X_train,y_train)
# print(log_reg.score(X_test,y_test))#1.0
#
# print(log_reg.predict_proba(X_test))
# #[0.92972035 0.98664939 0.14852024 0.01685947 0.0369836  0.0186637
#  # 0.04936918 0.99669244 0.97993941 0.74524655 0.04473194 0.00339285
#  # 0.26131273 0.0369836  0.84192923 0.79892262 0.82890209 0.32358166
#  # 0.06535323 0.20735334]
#
# print(log_reg.coef_) #[ 3.01796521 -5.04447145]
# print(log_reg.intercept_) #-0.6937719272911225

#因为就选了两个特征，可以观察x和y的关系对最终结果的影响范围
def x2(x1):
    return (-log_reg.coef_[0]*x1-log_reg.intercept_)/log_reg.coef_[1]
x1_plot = np.linspace(4,8,100)
x2_plot = x2(x1_plot)

# plt.scatter(X_test[y_test==0,0], X_test[y_test==0,1], color="red")
# plt.scatter(X_test[y_test==1,0], X_test[y_test==1,1], color="blue")
# plt.plot(x1_plot, x2_plot)
# plt.show()

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


# plot_decision_boundary(log_reg, axis=[4, 7.5, 1.5, 4.5])
# plt.scatter(X[y == 0, 0], X[y == 0, 1])
# plt.scatter(X[y == 1, 0], X[y == 1, 1])
# plt.show()

from sklearn.neighbors import KNeighborsClassifier
knn_clf = KNeighborsClassifier()
knn_clf.fit(X,y)
# plot_decision_boundary(knn_clf, axis=[4, 7.5, 1.5, 4.5])
# plt.scatter(X[y==0,0], X[y==0,1])
# plt.scatter(X[y==1,0], X[y==1,1])
# plt.show()

knn_clf_all = KNeighborsClassifier(n_neighbors=50)
knn_clf_all.fit(iris.data[:,:2],iris.target)

# plot_decision_boundary(knn_clf_all, axis=[4, 8, 1.5, 4.5])
# plt.scatter(iris.data[iris.target==0,0], iris.data[iris.target==0,1])
# plt.scatter(iris.data[iris.target==1,0], iris.data[iris.target==1,1])
# plt.scatter(iris.data[iris.target==2,0], iris.data[iris.target==2,1])
# plt.show()


np.random.seed(666)
X = np.random.normal(0, 1, size=(200, 2))#两个特征值
y = np.array((X[:,0]**2+X[:,1]**2)<1.5, dtype='int') #逻辑回归中只有两类

# plt.scatter(X[y==0,0], X[y==0,1])
# plt.scatter(X[y==1,0], X[y==1,1])
# plt.show()

# log_reg = LogisticRegression()
# log_reg.fit(X,y)
# print(log_reg.score(X,y)) #0.605,分值很低因为当做了简单一次函数处理
# print(log_reg.coef_,log_reg.intercept_) #[ 0.13862213 -0.05142173] 0.25844208169040384
#
# plot_decision_boundary(log_reg, axis=[-4, 4, -4, 4])
# plt.scatter(X[y==0,0], X[y==0,1])
# plt.scatter(X[y==1,0], X[y==1,1])
# plt.show()


#多项式逻辑回归
from sklearn.preprocessing import PolynomialFeatures
from sklearn.preprocessing import  StandardScaler
from sklearn.pipeline import Pipeline

def PolynomialLogisticRegression(degree):
    return Pipeline([
        ('poly', PolynomialFeatures(degree=degree)),
        ('std_scaler', StandardScaler()),
        ('log_reg', LogisticRegression())
    ])

log_reg2 = PolynomialLogisticRegression(degree=2)
log_reg2.fit(X,y)
# print(log_reg2.score(X,y))#0.95 用多项式处理时正确率就会提高

# plot_decision_boundary(log_reg2, axis=[-4, 4, -4, 4])
# plt.scatter(X[y==0,0], X[y==0,1])
# plt.scatter(X[y==1,0], X[y==1,1])
# plt.show()



#正则化
np.random.seed(666)
X = np.random.normal(0, 1, size=(200, 2))
y = np.array((X[:,0]**2+X[:,1])<1.5, dtype='int') #一次和二次都有
for _ in range(20):#更改一些y值，添加噪音
    y[np.random.randint(200)] = 1

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=666)

from sklearn.linear_model import LogisticRegression
def PolynomialLogisticRegression(degree, C, penalty='l2'):
    return Pipeline([
        ('poly', PolynomialFeatures(degree=degree)),
        ('std_scaler', StandardScaler()),
        ('log_reg', LogisticRegression(C=C,penalty=penalty))
    ])

poly_log_reg = PolynomialLogisticRegression(degree=20, C=0.1,penalty='l2')
poly_log_reg.fit(X_train, y_train)
# print(poly_log_reg.score(X_train, y_train))#0.8533333333333334
# print(poly_log_reg.score(X_test,y_test)) #0.92
# plot_decision_boundary(poly_log_reg, axis=[-4, 4, -4, 4])
# plt.scatter(X[y==0,0], X[y==0,1])
# plt.scatter(X[y==1,0], X[y==1,1])
# plt.show()
#
from sklearn import datasets
digits = datasets.load_digits()
X = digits.data
y = digits.target

#逻辑回归自带的是OvR不需要加参数
reg = LogisticRegression()
reg.fit(X,y)
print(reg.score(X,y)) # 0.993322203672788

#OvO需要在逻辑回归上加参数
reg2 = LogisticRegression(multi_class="multinomial", solver="newton-cg")
reg2.fit(X,y)
print(reg2.score(X,y)) # 1.0

