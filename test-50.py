# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.datasets import load_iris
# from sklearn.cluster import KMeans
# kms = KMeans(n_clusters=3)
# data = load_iris().data
# target = load_iris().target
# y=kms.fit_predict(data)
# print(y)
# s=np.arange(0,len(y))
# plt.scatter(s,y)
# plt.show()



from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt


a=[]
for i in range(100):
    with open('text/text{}.txt'.format(i),'r')as f:
        a.append(f.read())

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(a)

transformer = TfidfTransformer()
tfidf = transformer.fit_transform(X)

# print(tfidf.toarray())
km = KMeans(n_clusters=5)
y=km.fit_predict(tfidf.toarray())
s=np.arange(0,len(y))
plt.scatter(s,y)
plt.show()










