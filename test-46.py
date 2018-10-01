import jieba
from gensim import corpora,models,similarities
from collections import defaultdict

doc0 = "我不喜欢上海"
doc1 = "上海是一个好地方"
doc2 = "北京是一个好地方"
doc3 = "上海好吃的在哪里"
doc4 = "上海好玩的在哪里"
doc5 = "上海是好地方"
doc6 = "上海路和上海人"
doc7 = "喜欢小吃"
doc_test="我喜欢上海的小吃"

all_doc = []
all_doc.append(doc0)
all_doc.append(doc1)
all_doc.append(doc2)
all_doc.append(doc3)
all_doc.append(doc4)
all_doc.append(doc5)
all_doc.append(doc6)
all_doc.append(doc7)

# 对目标文档进行分词，并且保存在列表all_doc_list中
all_doc_list = []
for doc in all_doc:
    doc_list = [word for word in jieba.cut(doc)]
    all_doc_list.append(doc_list)

frequency = defaultdict(int)
for text in all_doc_list:
    for token in text:
        frequency[token] += 1  # 统计出各个词的出现次数

# 只保留大于10次的词
texts = [[token for token in text if frequency[token] > 10] for text in all_doc_list]

# 把测试文档也进行分词，并保存在列表doc_test_list中
doc_test_list = [word for word in jieba.cut(doc_test)]

# 用dictionary方法获取词袋
dictionary = corpora.Dictionary(all_doc_list)

# 使用doc2bow制作语料库
corpus = [dictionary.doc2bow(doc) for doc in all_doc_list]
# 把测试文档也转换为二元组的向量
doc_test_vec = dictionary.doc2bow(doc_test_list)

#用TF-IDF模型对语料库建模
tfidf = models.TfidfModel(corpus)
# 每个目标文档，分析测试文档的相似度
index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=len(dictionary.keys()))
sim = index[tfidf[doc_test_vec]]
print(sorted(enumerate(sim), key=lambda item: -item[1]))

