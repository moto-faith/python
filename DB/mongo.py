from pymongo import *
# 连接
client = MongoClient(host='localhost', port=27017)
# 选择库
db = client.test
# 选择集合
test_set = db.test
# 增
test_set.insert({"name":"ki", 'age':22})
test_set.insert({"name":"tom", 'age':22})
# 查
for result in test_set.find({'age':22}):
    print(result)
# 删
test_set.remove({'name':'ki'})
# 改
test_set.update({'name':'tom','age':22},{'name':'peter','age':24})