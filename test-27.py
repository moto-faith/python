#MNIST 数据库分类
import numpy as np
from sklearn.datasets import fetch_mldata
import time
mnist = fetch_mldata('MNIST original')
X,y = mnist['data'],mnist['target']
X_train = np.array(X[:60000],dtype=float)
X_test = np.array(X[60000:],dtype=float)
y_train = np.array(y[:60000],dtype=float)
y_test = np.array(y[60000:],dtype=float)

# print(X_train.shape)#(60000, 784) 这是一个784维的数据

#使用KNN分类
from sklearn.neighbors import KNeighborsClassifier
knn_clf = KNeighborsClassifier()
time1 = time.time()
knn_clf.fit(X_train,y_train)
print(knn_clf.score(X_test,y_test)) #0.9688
time2 = time.time()
print(time2-time1) #902.0233969688416

#先降维再分类
from sklearn.decomposition import PCA
pca = PCA(0.9)#方差正确率为0.9
pca.fit(X_train)
X_train_reduction = pca.transform(X_train)
X_test_reduction = pca.transform(X_test)
knn_clf = KNeighborsClassifier()
time3 = time.time()
knn_clf.fit(X_train_reduction,y_train)
print(knn_clf.score(X_test_reduction,y_test)) #0.9728
time4 = time.time()
print(time4-time3) #116.10433602333069















