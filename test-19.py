from model_selection import   train_test_split
import numpy as np
from sklearn import  datasets
# from KNN import KNNClassifier


iris=datasets.load_iris()
# print(iris.keys())
x=iris.data
y=iris.target
#
# x_train,x_test,y_train,y_test = train_test_split(x,y)
#
# my_knn=KNNClassifier(k=3)
# my_knn.fit(x_train,y_train)
# y_predict=my_knn.predict(x_test)
# print(y_test)
# print(y_predict)
# print(sum(y_predict==y_test)/len(y_test))

#########################################################
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
# kNN_classifier  = KNeighborsClassifier(n_neighbors=3)
# kNN_classifier.fit(x_train,y_train)
# y_predict = kNN_classifier.predict(x_test)
# # print(sum(y_predict==y_test)/len(y_test))
#
#
# best_score = 0.0
# best_k = -1
# best_p = -1
#
# for k in range(1, 11):
#     for p in range(1, 6):
#         knn_clf = KNeighborsClassifier(n_neighbors=k, weights="distance", p=p)#考虑了P就确定了考虑了距离,所以weights="distance"
#         knn_clf.fit(x_train, y_train)
#         score = knn_clf.score(x_test, y_test)
#         if score > best_score:
#             best_k = k
#             best_p = p
#             best_score = score
#
# print("best_k =", best_k)
# print("best_p =", best_p)
# print("best_score =", best_score)

from preprocessing import StandardScaler
standardScaler = StandardScaler()
standardScaler.fit(x_train)
# print(standardScaler.mean_)#平均值
# print(standardScaler.scale_)#方差

x_train=standardScaler.transform(x_train)#把所有数值归一化,用的是x_train的平均值方差
# print(x_train)
x_test_standard = standardScaler.transform(x_test)#用的还是x_train的平均值方差

knn_clf = KNeighborsClassifier(n_neighbors=3)#把归一化的数据代如KNN算法
knn_clf.fit(x_train,y_train)
print(knn_clf.score(x_test_standard,y_test))#得到结果0.9666666666666667



