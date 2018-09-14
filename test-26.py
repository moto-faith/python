# #从高维数据向低维数据的映射
# import numpy as np
# import matplotlib.pyplot as plt
# X = np.empty((100, 2))
# X[:,0] = np.random.uniform(0., 100., size=100)
# X[:,1] = 0.75 * X[:,0] + 3. + np.random.normal(0, 10., size=100)
#
# from PCA import PCA
# pca = PCA(n_components=2)
# pca.fit(X)
# print(pca.components_)#[[ 0.76018413  0.64970769] [-0.64970246  0.76018861]]
#
# pca = PCA(n_components=1)
# pca.fit(X)
# X_reduction = pca.transform(X)#转化为在第一主成分里的位置
#
# X_restore = pca.inverse_transform(X_reduction)#把第一主成分位置转化回两个特征值
#
# plt.scatter(X[:,0], X[:,1], color='b', alpha=0.5)
# plt.scatter(X_restore[:,0], X_restore[:,1], color='r', alpha=0.5)
# plt.show()
#
# from sklearn.decomposition import  PCA
# pca = PCA(n_components=1)
# pca.fit(X)
# print(pca.components_)
# X_reduction = pca.transform(X)
# X_restore = pca.inverse_transform(X_reduction)
# plt.scatter(X[:,0], X[:,1], color='b', alpha=0.5)
# plt.scatter(X_restore[:,0], X_restore[:,1], color='r', alpha=0.5)
# plt.show()

#使用数字图像数据来降维分类
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
import time
digits = datasets.load_digits()
X = digits.data
y = digits.target

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=666)
# print(X_train.shape)#(1347, 64) 这是64维的数据

#使用KNN算法不降维来分类
time1 = time.time()
from sklearn.neighbors import KNeighborsClassifier
knn_clf = KNeighborsClassifier()
knn_clf.fit(X_train,y_train)
print(knn_clf.score(X_test,y_test)) #0.9866666666666667
time2 = time.time()
print(time2-time1) #  0.10456466674804688

#先降维再分类
from sklearn.decomposition import PCA
time3 = time.time()
pca = PCA(n_components=2)#降为2维
pca.fit(X_train)
X_train_rediction = pca.transform(X_train)
X_test_rediction = pca.transform(X_test)
knn_clf = KNeighborsClassifier()
knn_clf.fit(X_train_rediction,y_train)
print(knn_clf.score(X_test_rediction,y_test)) #0.6066666666666667
time4 = time.time()
print(time4-time3) #0.007133007049560547

#先降维虽然时间缩短但是准确度降低了，需要重新设置维度
print(pca.explained_variance_ratio_)#在两维时每个维度正确率为 [0.14566817 0.13735469]，数值过于偏大

#设置为64维时，看每个维度的方差正确率
from sklearn.decomposition import PCA
pca = PCA(n_components=X_train.shape[1])
pca.fit(X_train)
# print(pca.explained_variance_ratio_)
'''
[1.45668166e-01 1.37354688e-01 1.17777287e-01 8.49968861e-02
 5.86018996e-02 5.11542945e-02 4.26605279e-02 3.60119663e-02
 3.41105814e-02 3.05407804e-02 2.42337671e-02 2.28700570e-02
 1.80304649e-02 1.79346003e-02 1.45798298e-02 1.42044841e-02
 1.29961033e-02 1.26617002e-02 1.01728635e-02 9.09314698e-03
 8.85220461e-03 7.73828332e-03 7.60516219e-03 7.11864860e-03
 6.85977267e-03 5.76411920e-03 5.71688020e-03 5.08255707e-03
 4.89020776e-03 4.34888085e-03 3.72917505e-03 3.57755036e-03
 3.26989470e-03 3.14917937e-03 3.09269839e-03 2.87619649e-03
 2.50362666e-03 2.25417403e-03 2.20030857e-03 1.98028746e-03
 1.88195578e-03 1.52769283e-03 1.42823692e-03 1.38003340e-03
 1.17572392e-03 1.07377463e-03 9.55152460e-04 9.00017642e-04
 5.79162563e-04 3.82793717e-04 2.38328586e-04 8.40132221e-05
 5.60545588e-05 5.48538930e-05 1.08077650e-05 4.01354717e-06
 1.23186515e-06 1.05783059e-06 6.06659094e-07 5.86686040e-07
 1.71368535e-33 7.44075955e-34 7.44075955e-34 7.15189459e-34]
'''

#把正确率累加，看维度到多少时，错误率可以被接受
plt.plot([i for  i in range(X_train.shape[1])],
         [np.sum(pca.explained_variance_ratio_[:i+1]) for i in range(X_train.shape[1])])
plt.show()

#设置方差正确率，由方差正确率得出应设置的维度
pca = PCA(0.95)
pca.fit(X_train)
print(pca.n_components_) #28
X_train_rediction = pca.transform(X_train)
X_test_rediction = pca.transform(X_test)
time5 =time.time()
knn_clf = KNeighborsClassifier()
knn_clf.fit(X_train_rediction,y_train)
print(knn_clf.score(X_test_rediction,y_test)) #0.98
time6 =time.time()
print(time6-time5)#0.02398967742919922
#在耗时减少的前提下也提高了正确率