import numpy as np
from sklearn import datasets
boston = datasets.load_boston()

X = boston.data
y = boston.target
# print(boston.feature_names)
X = X[y < 50.0]#导入了多元数据
y = y[y < 50.0]


# from  model_selection import train_test_split
#
# X_train, X_test, y_train, y_test = train_test_split(X, y, seed=666)#分割数据为训练集和测试集


# from LinearRegression import LinearRegression #自己写的多元线性回归算法
#
# reg = LinearRegression()
# reg.fit_normal(X_train,y_train)
# print(reg.coef_) #系数
# print(reg.intercept_) #截距
#
# print(reg.score(X_test,y_test)) #0.8129794056212711

from sklearn.linear_model import LinearRegression
reg = LinearRegression()
reg.fit(X,y)

print(boston.feature_names[np.argsort(reg.coef_)])
'''
['NOX' 'DIS' 'PTRATIO' 'LSTAT' 'CRIM' 'INDUS' 'AGE' 'TAX' 'B' 'ZN' 'RAD'
 'CHAS' 'RM']越靠前的是负相关，靠后的是正相关
'''

# print(reg.coef_)#系数
# print(reg.intercept_) #截距
# print(reg.score(X_test,y_test))#0.8129794056212811

# #首先对数据进行归一
# from sklearn.preprocessing import StandardScaler
# standardScaler = StandardScaler()
# standardScaler.fit(X_train,y_train)
# X_train_standard = standardScaler.transform(X_train)
# X_test_standard = standardScaler.transform(X_test)
#
# #然后训练模型,导入的是KNN的回归包，而不是分类包
# from sklearn.neighbors import KNeighborsRegressor
# knn_reg = KNeighborsRegressor()
# knn_reg.fit(X_train_standard,y_train)
# print(knn_reg.score(X_test_standard,y_test)) #0.847923904906593
#
# #还可以通过调整超参数，网格搜索来找到最佳参数
# from sklearn.model_selection import GridSearchCV
# param_grid = [
#     {
#         "weights": ["uniform"],
#         "n_neighbors": [i for i in range(1, 11)]
#     },
#     {
#         "weights": ["distance"],
#         "n_neighbors": [i for i in range(1, 11)],
#         "p": [i for i in range(1,6)]
#     }
# ]
# knn_reg = KNeighborsRegressor()
# grid_search = GridSearchCV(knn_reg,param_grid,n_jobs=-1,verbose=2)
# grid_search.fit(X_train_standard,y_train)
# print(grid_search.best_params_)#最佳参数 {'n_neighbors': 5, 'p': 1, 'weights': 'distance'}
# print(grid_search.best_score_)#最佳正确率 0.7991317809214437
# print(grid_search.best_estimator_.score(X_test_standard, y_test)) #在最佳条件下测试集的正确率 0.8814052328522632

