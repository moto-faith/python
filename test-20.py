import numpy as np
from sklearn import datasets
import matplotlib.pyplot as plt
import matplotlib

digits = datasets.load_digits()
x=digits.data
y=digits.target
# plt.imshow(x[600].reshape(8,8), cmap = matplotlib.cm.binary)
# plt.show()
# print(y[600])
# from model_selection import train_test_split
# x_train,x_test,y_train,y_test = train_test_split(x,y,test_ratio=0.2)
#
# from KNN import KNNClassifier
# kNN_clf = KNNClassifier(3)
# kNN_clf.fit(x_train,y_train)
# # y_predict =  kNN_clf.predict(x_test)
# # print(sum(y_predict==y_test)/len(y_test)) #0.9972144846796658
# # print(kNN_clf.score(x_test,y_test)) #0.9860724233983287
#
# print(kNN_clf.score(x_test,y_test))#0.9888579387186629

from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=666)
from sklearn.neighbors import KNeighborsClassifier

# sk_knn_clf = KNeighborsClassifier(n_neighbors=4, weights="uniform")
# sk_knn_clf.fit(x_train, y_train)
# sk_knn_clf.score(x_test, y_test)

#把各种超参数组成一个字典来循环遍历，找到最优解
# param_grid = [
#     {
#         'weights': ['uniform'],
#         'n_neighbors': [i for i in range(1, 11)]
#     },
#     {
#         'weights': ['distance'],
#         'n_neighbors': [i for i in range(1, 11)],
#         'p': [i for i in range(1, 6)]
#     }
# ]
# knn_clf = KNeighborsClassifier()
# from sklearn.model_selection import GridSearchCV
# #n_jobs为参与计算的核心数量，-1为所有核，verbose为过程打印
# grid_search = GridSearchCV(knn_clf,param_grid,n_jobs=-1,verbose=3)
# grid_search.fit(x_train,y_train)
# print(grid_search.best_estimator_)#最优的参数
# print(grid_search.best_score_)#最高的正确率

x=np.random.randint(0,100,(50,2))
x=np.array(x,dtype=float) #因为最后转化的值为0到1之间，所以转换类型为浮点
# x[:,0]=(x[:,0]-np.min(x[:,0]))/(np.max(x[:,0])-np.min(x[:,0]))
# x[:,1]=(x[:,1]-np.min(x[:,1]))/(np.max(x[:,1])-np.min(x[:,1]))
# # print(x)
# plt.scatter(x[:,0],x[:,1])
# plt.show()
#
x[:,0]=(x[:,0]-np.mean(x[:,0]))/np.std(x[:,0])
x[:,1]=(x[:,1]-np.mean(x[:,1]))/np.std(x[:,1])
plt.scatter(x[:,0],x[:,1])
plt.show() #均值接近0，方差接近1






