import numpy as np
from sklearn.datasets import load_iris
from keras.models import Sequential
from keras.layers.core import  Dense,Activation

iris = load_iris()
data = iris.data
target = iris.target
data = data[target<2]
target = target[target<2]

model = Sequential()
# 输入层
model.add(Dense(10,input_dim=4))
model.add(Activation('relu'))
# 输出层
model.add(Dense(1,input_dim=1))
model.add(Activation('sigmoid'))
# 模型的编译
model.compile(loss='mean_squared_error',optimizer='adam')
# 训练
model.fit(data,target,nb_epoch=1000,batch_size=6)
# 预测
rst = model.predict_classes(data)
print(rst.reshape(len(target)))
print(target)


















