# 集成学习
import numpy as np
import matplotlib.pyplot as plt

from sklearn import datasets
X,y = datasets.make_moons(n_samples=500,noise=0.3,random_state=42)
# plt.scatter(X[y==0,0],X[y==0,1])
# plt.scatter(X[y==1,0],X[y==1,1])
# plt.show()

from sklearn.model_selection import  train_test_split
X_train,X_test,y_train,y_test = train_test_split(X,y,random_state=42)

from sklearn.linear_model import LogisticRegression
log_clf = LogisticRegression()
log_clf.fit(X_train,y_train)

from sklearn.svm import SVC
svm_clf = SVC()
svm_clf.fit(X_train,y_train)

from sklearn.tree import DecisionTreeClassifier
dt_clf = DecisionTreeClassifier()
dt_clf.fit(X_train,y_train)

y_predict1 = log_clf.predict(X_test)
y_predict2 = svm_clf.predict(X_test)
y_predict3 = dt_clf.predict(X_test)

# 三种方法的预测结果取大于等于两个相同的结果
y_predict = np.array((y_predict1 + y_predict2 + y_predict3) >= 2, dtype='int')
# print(log_clf.score(X_test,y_test)) # 0.864
# print(svm_clf.score(X_test,y_test))# 0.888
# print(dt_clf.score(X_test,y_test)) # 0.848
from sklearn.metrics import accuracy_score
# print(accuracy_score(y_test,y_predict)) # 0.896

# 使用Voting Classifier
from sklearn.ensemble import VotingClassifier
voting_clf = VotingClassifier(estimators=[
    ('log_clf',LogisticRegression()),
    ('svm_clf',SVC()),
    ('dt_clf',DecisionTreeClassifier(random_state=666))],
                      voting= 'hard')
voting_clf.fit(X_train,y_train)
# print(voting_clf.score(X_test,y_test)) # 0.896

voting_clf2 = VotingClassifier(estimators=[
    ('log_clf',LogisticRegression()),
    ('svm_clf',SVC(probability=True)),# SVC默认不计算概率，需要设置
    ('dt_clf',DecisionTreeClassifier(random_state=666))],
                      voting= 'soft')
voting_clf2.fit(X_train,y_train)
# print(voting_clf2.score(X_test,y_test))# 0.912

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
#用决策树算法，训练500个模型，每个模型取样100个，采用放回取样方式
bagging_clf = BaggingClassifier(DecisionTreeClassifier(),
                                n_estimators=500,max_samples=100,
                                bootstrap=True)
bagging_clf.fit(X_train,y_train)
# print(bagging_clf.score(X_test,y_test)) # 0.912

bagging_clf2 = BaggingClassifier(DecisionTreeClassifier(),
                                n_estimators=5000,max_samples=100,
                                bootstrap=True)
bagging_clf2.fit(X_train,y_train)
# print(bagging_clf2.score(X_test,y_test)) #


bagging_clf = BaggingClassifier(DecisionTreeClassifier(),
                                n_estimators=500,max_samples=100,
                                bootstrap=True,oob_score=True)
bagging_clf.fit(X,y)
# print(bagging_clf.oob_score_)# 0.918

# max_features是最多随机抽取的特征数（列数），bootstrap_features是抽取随机特征
bagging_clf3 = BaggingClassifier(DecisionTreeClassifier(),
                                n_estimators=500,max_samples=100,
                                bootstrap=True,oob_score=True,
                                max_features=1,bootstrap_features=True)
bagging_clf3.fit(X,y)
# print(bagging_clf3.oob_score_)# 0.856

from sklearn.ensemble import RandomForestClassifier
tf_clf = RandomForestClassifier(n_estimators=500,max_leaf_nodes=16,oob_score=True, random_state=666, n_jobs=-1)
tf_clf.fit(X,y)
# print('tf',tf_clf.oob_score_) #0.92

from sklearn.ensemble import ExtraTreesClassifier
et_clf = ExtraTreesClassifier(n_estimators=500, bootstrap=True, oob_score=True, random_state=666, n_jobs=-1)
et_clf.fit(X,y)
# print('et',et_clf.oob_score_) #0.892


from sklearn.ensemble import AdaBoostClassifier
ada_clf = AdaBoostClassifier(DecisionTreeClassifier(max_depth=2),n_estimators=500)
ada_clf.fit(X_train,y_train)
print(ada_clf.score(X_test,y_test))# 0.832

from sklearn.ensemble import GradientBoostingClassifier
gb_clf = GradientBoostingClassifier(max_depth=2,n_estimators=30)
gb_clf.fit(X_train,y_train)
print(gb_clf.score(X_test,y_test))# 0.912