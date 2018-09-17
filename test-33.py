# 精准率 召回率曲线，F1score，FPR,TPR
import numpy as np
from sklearn import datasets
digits = datasets.load_digits()
X = digits.data
y = digits.target.copy()



from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.8,random_state=666)

from sklearn.linear_model import LogisticRegression
reg = LogisticRegression()
reg.fit(X_train,y_train)
# print(reg.score(X_test,y_test)) #0.9755555555555555

y_predict = reg.predict(X_test)

def TN(y_true, y_predict):
    assert len(y_true) == len(y_predict)
    return np.sum((y_true == 0) & (y_predict == 0))

def TP(y_true, y_predict):
    assert len(y_true) == len(y_predict)
    return np.sum((y_true == 1) & (y_predict == 1))

def FN(y_true, y_predict):
    assert len(y_true) == len(y_predict)
    return np.sum((y_true == 1) & (y_predict == 0))

def FP(y_true, y_predict):
    assert len(y_true) == len(y_predict)
    return np.sum((y_true == 0) & (y_predict == 1))

def confusion_matrix(y_true, y_predict):
    return np.array([
        [TN(y_true, y_predict), FP(y_true, y_predict)],
        [FN(y_true, y_predict), TP(y_true, y_predict)]
    ])

# print(confusion_matrix(y_test,y_predict))
# # [[403   2]
# #  [  9  36]]

#准确率
def precision_score(y_true, y_predict):
    tp = TP(y_true, y_predict)
    fp = FP(y_true, y_predict)
    try:
        return tp / (tp + fp)
    except:
        return 0.0

#召回率
def recall_score(y_true, y_predict):
    tp = TP(y_true, y_predict)
    fn = FN(y_true, y_predict)
    try:
        return tp / (tp + fn)
    except:
        return 0.0

# print(precision_score(y_test,y_predict)) #0.9473684210526315
# print(recall_score(y_test,y_predict))  #0.8

#sklearn中的混淆矩阵 精准率 召回率
from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
# print(confusion_matrix(y_test,y_predict))
# [[403   2]
#  [  9  36]]
# print(precision_score(y_test,y_predict)) 0.9473684210526315
# print(recall_score(y_test,y_predict)) 0.8

def f1_score(precision,recall):
    try:
        return 2 * precision * recall / (precision + recall)
    except:
        return 0.0

# print(f1_score(precision_score(y_test,y_predict),recall_score(y_test,y_predict))) 0.8674698795180723

from sklearn.metrics import f1_score
# print(f1_score(y_test,y_predict)) 0.8674698795180723

# print(reg.decision_function(X_test)[:10])
# [-22.05705181 -33.02949573 -16.21340238 -80.37917009 -48.25125209
#  -24.54010044 -44.39166152 -25.04298784  -0.97831701 -19.71745321]
decision_scores = reg.decision_function(X_test)
# print(np.max(decision_score)) 19.889573725637934
# print(np.min(decision_score)) -85.68617092628044
y_predict_2 = np.array(decision_scores >= 5, dtype='int')
# print(precision_score(y_test,y_predict_2)) 0.96
# print(recall_score(y_test,y_predict_2)) 0.5333333333333333
# print(confusion_matrix(y_test,y_predict_2))
# [[404   1]
#  [ 21  24]]

# # 精准度-召回率曲线
import matplotlib.pyplot as plt
# from sklearn.metrics import precision_score
# from  sklearn.metrics import recall_score
# precisions = []
# recalls = []
# threshoulds = np.arange(np.min(decision_scores),np.max(decision_scores),0.1)
# for theshould in threshoulds:
#     y_predict = np.array(decision_scores>=theshould,dtype='int')# 算出每个边界值的预测y
#     precisions.append(precision_score(y_test,y_predict))# 算出每次预测y的精准值
#     recalls.append(recall_score(y_test,y_predict))# 算出每次预测y的召回率

# #每次的threshould对应的精准度和召回率的图
# plt.plot(threshoulds,precisions)
# plt.plot(threshoulds,recalls)
# plt.show()
#
# # 精准度和召回率的变化关系是相互制约的
# plt.plot(precisions,recalls)
# plt.show()

# from sklearn.metrics import precision_recall_curve
# precisions, recalls, threshoulds = precision_recall_curve(y_test, decision_scores)

#每次的threshould对应的精准度和召回率的图
# print(precisions[-1]) #1.0
#因为精准度和召回率的最后一个值都是1，数组数量比thershoulds多一个，需去掉
# plt.plot(threshoulds,precisions[:-1])
# plt.plot(threshoulds,recalls[:-1])
# plt.show()
#
# # 精准度和召回率的变化关系是相互制约的
# plt.plot(precisions,recalls)
# plt.show()

# from metrics import FPR,TPR
# fprs = []
# tprs = []
# threshoulds = np.arange(np.min(decision_scores),np.max(decision_scores),0.1)
# for threshould in threshoulds:
#     y_predict = np.array(decision_scores>=threshould,dtype='int')
#     fprs.append(FPR(y_test,y_predict))
#     tprs.append(TPR(y_test,y_predict))
# plt.plot(fprs,tprs)
# plt.show()
#
# from sklearn.metrics import roc_curve
# fprs, tprs, thresholds = roc_curve(y_test, decision_scores)
# plt.plot(fprs,tprs)
# plt.show()
#
# from sklearn.metrics import roc_auc_score
# print(roc_auc_score(y_test,decision_scores)) # 0.9830452674897119


# 把测试集比例调整为0.8
from sklearn.metrics import precision_score
print(precision_score(y_test,y_predict,average='micro')) #0.93115438108484

from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test,y_predict))
# [[147   0   1   0   0   1   0   0   0   0]
#  [  0 123   1   2   0   0   0   3   4  10]
#  [  0   0 134   1   0   0   0   0   1   0]
#  [  0   0   0 138   0   5   0   1   5   0]
#  [  2   5   0   0 139   0   0   3   0   1]
#  [  1   3   1   0   0 146   0   0   1   0]
#  [  0   2   0   0   0   1 131   0   2   0]
#  [  0   0   0   1   0   0   0 132   1   2]
#  [  1   9   2   3   2   4   0   0 115   4]
#  [  0   1   0   5   0   3   0   2   2 134]]


cfm = confusion_matrix(y_test, y_predict)
plt.matshow(cfm, cmap=plt.cm.gray)
plt.show()


#可看出有很多‘1’预测成了‘9’，很多‘8’预测成了‘1’
row_sums = np.sum(cfm, axis=1)
err_matrix = cfm / row_sums
np.fill_diagonal(err_matrix, 0)

plt.matshow(err_matrix, cmap=plt.cm.gray)
plt.show()