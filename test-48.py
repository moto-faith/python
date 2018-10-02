#coding:utf-8
# 朴素贝叶斯算法
import pandas as pd
import numpy as np
import sklearn.datasets

class NaiveBayes(object):

    def classify(self, trainData, labels, features):
        #求labels中每个label的先验概率
        labels = list(labels)    #转换为list类型
        P_y = {}       #存入label的概率
        for label in labels:
            P_y[label] = labels.count(label)/float(len(labels))   # p = count(y) / count(Y)

        #求label与feature同时发生的概率
        P_xy = {}
        for y in P_y.keys():
            y_index = [i for i, label in enumerate(labels) if label == y]  # labels中出现y值的所有数值的下标索引
            for j in range(len(features)):      # features[0] 在trainData[:,0]中出现的值的所有下标索引
                x_index = [i for i, feature in enumerate(trainData[:,j]) if feature == features[j]]
                xy_count = len(set(x_index) & set(y_index))   # set(x_index)&set(y_index)列出两个表相同的元素
                pkey = str(features[j]) + '*' + str(y)
                P_xy[pkey] = xy_count / float(len(labels))

        #求条件概率
        P = {}
        for y in P_y.keys():
            for x in features:
                pkey = str(x) + '|' + str(y)
                P[pkey] = P_xy[str(x)+'*'+str(y)] / float(P_y[y])    #P[X1/Y] = P[X1Y]/P[Y]

        #求所属类别
        F = {}
        for y in P_y:
            F[y] = P_y[y]
            for x in features:
                F[y] = F[y]*P[str(x)+'|'+str(y)]     #P[y/X] = P[X/y]*P[y]/P[X]，分母相等，比较分子即可，所以有F=P[X/y]*P[y]=P[x1/Y]*P[x2/Y]*P[y]

        features_label = max(F, key=F.get)  #概率最大值对应的类别
        return features_label


if __name__ == '__main__':
    Data = sklearn.datasets.load_iris()
    trainData = Data.data
    labels = Data.target
    nb = NaiveBayes()

    features = [2,2,1,1]
    # 该特征应属于哪一类
    result = nb.classify(trainData, labels, features)
    print (features,'属于',result)