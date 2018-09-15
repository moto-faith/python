# #多项式回归，交叉验证
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.random.uniform(-3,3,size=100)
# X = x.reshape(-1,1)#一个特征100个样本
# y = 0.5 * x**2 + x + 2 +np.random.normal(0,1,100)
# # plt.scatter(X,y)
# # plt.show()
#
# from sklearn.linear_model import LinearRegression
# reg = LinearRegression()
# reg.fit(X,y)
# y_predict = reg.predict(X)
# # plt.scatter(X,y)
# # plt.plot(X,y_predict,color = 'r')
# # plt.show()
#
# X2 = np.hstack([X,X**2])
# # print(X2.shape) #(100, 2)增加了一列特征值：X**2
# reg2 = LinearRegression()
# reg2.fit(X2,y)
# y_predict2 = reg2.predict(X2)
# plt.scatter(x,y)
# plt.plot(np.sort(x),y_predict2[np.argsort(x)],color = 'r')#由于x并不是有序数组，所以连线会乱，因此需要先排序再连线
# plt.show()
# print(reg2.coef_)#x的系数和X**2的系数[0.99158261 0.51495067]
# print(reg2.intercept_)#截距1.9865604994175838
#
#
#scikit-learn中的多项式回归
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.random.uniform(-3, 3, size=100)
# X = x.reshape(-1, 1)
# y = 0.5 * x**2 + x + 2 + np.random.normal(0, 1, 100)
# from sklearn.preprocessing import PolynomialFeatures
# poly = PolynomialFeatures(degree=2)#设置最高为2次
# poly.fit(X)
# X2 = poly.transform(X)#把X转化成从0次到2次的数据
# # print(X2.shape) #(100, 3) 3中包含0次，1次和2次
#
# #把数据代入线性回归
# from sklearn.linear_model import LinearRegression
# reg = LinearRegression()
# reg.fit(X2,y)
# y_predict = reg.predict(X2)
# plt.scatter(x, y)
# plt.plot(np.sort(x), y_predict[np.argsort(x)], color='r')
# plt.show()
# print(reg.coef_)#[0.         0.94871319 0.47027173] X0次方的系数是0，一次方是0.94871319，二次方系数是0.47027173
# print(reg.intercept_)#截距为1.8350137866988987

# #pipline
# import numpy as np
# from sklearn.preprocessing import PolynomialFeatures
# from sklearn.linear_model import LinearRegression
# import matplotlib.pyplot as plt
#
# x = np.random.uniform(-3, 3, size=100)
# X = x.reshape(-1, 1)
# y = 0.5 * x**2 + x + 2 + np.random.normal(0, 1, 100)
#
# from sklearn.pipeline import Pipeline
# from sklearn.preprocessing import StandardScaler
#
# #把多步写为一步
# poly_reg = Pipeline([
#     ("poly", PolynomialFeatures(degree=300)),#加多项式系数
#     ("std_scaler", StandardScaler()),#数据归一化
#     ("lin_reg", LinearRegression())#线性回归
# ])
#
# poly_reg.fit(X,y)
# y_predict = poly_reg.predict(X)
# plt.scatter(x, y)
# plt.plot(np.sort(x), y_predict[np.argsort(x)], color='r')
# plt.show()

# import numpy as np
# import matplotlib.pyplot as plt
#
# np.random.seed(666)
# x = np.random.uniform(-3.0, 3.0, size=100)
# X = x.reshape(-1, 1)
# y = 0.5 * x**2 + x + 2 + np.random.normal(0, 1, size=100)
# # plt.scatter(X,y)
# # plt.show()
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=10)
#
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error
#
# train_score = []
# test_score = []
# for i in range(1, 76):#递增样本数量看MSE的曲线
#     lin_reg = LinearRegression()
#     lin_reg.fit(X_train[:i], y_train[:i])
#
#     y_train_predict = lin_reg.predict(X_train[:i])
#     #训练集的MSE
#     train_score.append(mean_squared_error(y_train[:i], y_train_predict))
#
#     y_test_predict = lin_reg.predict(X_test)
#     #测试集的MSE
#     test_score.append(mean_squared_error(y_test, y_test_predict))
#
# # plt.plot([i for i in range(1, 76)], np.sqrt(train_score), label="train")
# # plt.plot([i for i in range(1, 76)], np.sqrt(test_score), label="test")
# # plt.legend()
# # plt.axis([0, len(X_train)+1, 0, 4])
# # plt.show()
#
# from sklearn.preprocessing import PolynomialFeatures
# from sklearn.preprocessing import StandardScaler
# from sklearn.pipeline import Pipeline
# def PolynomialRegression(degree):
#     return Pipeline([
#         ("poly", PolynomialFeatures(degree=degree)),
#         ("std_scaler", StandardScaler()),
#         ("lin_reg", LinearRegression())
#     ])
#
#
# def plot_learning_curve(algo, X_train, X_test, y_train, y_test):
#     train_score = []
#     test_score = []
#     for i in range(1, len(X_train) + 1):
#         algo.fit(X_train[:i], y_train[:i])
#
#         y_train_predict = algo.predict(X_train[:i])
#         train_score.append(mean_squared_error(y_train[:i], y_train_predict))
#
#         y_test_predict = algo.predict(X_test)
#         test_score.append(mean_squared_error(y_test, y_test_predict))
#
#     plt.plot([i for i in range(1, len(X_train) + 1)],
#              np.sqrt(train_score), label="train")
#     plt.plot([i for i in range(1, len(X_train) + 1)],
#              np.sqrt(test_score), label="test")
#     plt.legend()
#     plt.axis([0, len(X_train) + 1, 0, 4])
#     plt.show()
#
# poly2_reg = PolynomialRegression(degree=20)
# plot_learning_curve(poly2_reg, X_train, X_test, y_train, y_test)


#手写数字数据交叉验证
import numpy as np
from  sklearn import datasets
digits = datasets.load_digits()
X = digits.data
y = digits.target

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=666)

from  sklearn.neighbors import KNeighborsClassifier

# #未使用交叉验证法(可能只是过度拟合了test数据)
best_k,best_p,best_score = 0,0,0
for k in range(2,11):
    for p in range(1,6):
        knn_clf = KNeighborsClassifier(weights='distance',n_neighbors=k,n_jobs=-1,p=p)
        knn_clf.fit(X_train,y_train)
        score = knn_clf.score(X_test,y_test)
        if score>best_score:
            best_k, best_p, best_score = k,p,score
print("k:",best_k)#k: 3
print('p:',best_p)#p: 4
print('score:',best_score) #score: 0.9860917941585535


#使用交叉验证法（经过交叉相当于多次验证而test不参与，p,k值更可信）
from sklearn.model_selection import cross_val_score

knn_clf = KNeighborsClassifier()
#自动把训练集分为三部分，两个训练一个验证，可组合为3组，得出三个score
score = cross_val_score(knn_clf,X_train,y_train)
print(score) #[0.98895028 0.97777778 0.96629213]
best_k, best_p, best_score = 0, 0, 0
for k in range(2, 11):
    for p in range(1, 6):
        knn_clf = KNeighborsClassifier(weights="distance", n_neighbors=k, p=p)
        scores = cross_val_score(knn_clf, X_train, y_train)
        score = np.mean(scores)
        if score > best_score:
            best_k, best_p, best_score = k, p, score

print("Best K =", best_k) #Best K = 2
print("Best P =", best_p) #Best P = 2
print("Best Score =", best_score) #Best Score = 0.9823599874006478

best_knn_clf = KNeighborsClassifier(weights="distance", n_neighbors=2, p=2)
best_knn_clf.fit(X_train, y_train)
print(best_knn_clf.score(X_test, y_test)) #0.980528511821975

