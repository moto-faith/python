from gensim import corpora, models, similarities
import jieba
from collections import defaultdict,Counter

d1 = open('text1.txt').read()
d2 = open('text1.txt').read()
d3 = open('text1.txt').read()
data1 = jieba.cut(d1)
data2 = jieba.cut(d2)
data3 = jieba.cut(d3)

data11 = ''
for i in data1:
    data11 += i + ' '
data21 = ''
for i in data2:
    data21 += i + ' '
data31 = ''
for i in data3:
    data31 += i + ' '

documents = [data11, data21]
texts = [[word for word in document.split()]for document in documents]

frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1  # 统计出各个词的出现次数

# 只保留大于10次的词
texts = [[token for token in text if frequency[token] > 10] for text in texts]

dictionary = corpora.Dictionary(texts)

new_vec = dictionary.doc2bow(data31.split())
corpus = [dictionary.doc2bow(text) for text in texts]
tridf = models.TfidfModel(corpus)
featureNum = len(dictionary.token2id.keys())
index = similarities.SparseMatrixSimilarity(
    tridf[corpus], num_features=featureNum)
sim = index[tridf[new_vec]]
print(new_vec)
