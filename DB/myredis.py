import redis
r = redis.Redis(host='localhost', port=6379, db=0)
# String 操作
# 增&改
r.set('name','345')
r.setrange('name',5,'a')
r.mset({"name1":'zhangsan', "name2":'lisi'})
r.setbit('name',6,0)# 二进制修改
r.incr('mont',amount=3)#执行一次自加3
r.decr('mout',amount=3)#执行一次自减3
r.append('name1','haha')#续写
# 查
print(r.get('name'))
print(r.getbit('name',0))
print(r.getrange('name1',0,3))
#删
r.delete('name')

#hash操作
#增&改
r.hset('dic_name','a1','aa')
r.hmset('dic_name',{'a2':'aa','a3':'bb'})
r.hincrby("dic_name","a",amount=2)#自增
#查
print(r.hget('dic_name','a1'))
print(r.hmget('dic_name',['a1','a2']))
print(r.hgetall('dic_name'))
print(r.hlen('dic_name'))
print(r.hexists('dic_name','a1'))
#删
r.hdel('dic_name','a1')

#list操作
#增
r.rpush('list_name',2,3,4,5)
r.lpush('list_name',1)
r.linsert('list_name','BEFORE',1,0)
#改
r.lset('list_name',0,-1)
r.lpop('list_name')
r.rpop('list_name')
r.rpoplpush('list_name','list_name')
#查
print(r.llen("list_name"))  # name对应的list元素的个数
print(r.lindex("list_name",1))  #根据索引获取列表内元素
print(r.lrange("list_name",0,-1))  #分片获取元素
#删
r.lrem("list_name",2,num=0)   #num=2 从前到后，删除2个；num=-2 从后向前，删除2个
r.ltrim("list_name",0,2)  #移除列表内没有在该索引之内的值

#set操作
#增&改
r.sadd('set_name','aa','bb','cc')
r.sadd('set_name1','aa','bb','cc')
r.smove('set_name','set_name1','aa')#移动
#删
r.spop('set_name')
r.srem('set_name1','aa')
#查
print(r.smembers('set_name'))
print(r.scard('set_name'))#元素数量
print(r.sdiff('set_name1','set_name'))#不同
print(r.sinter('set_name','set_name1'))#交集
print(r.sunion('set_name','set_name1'))#并集
print(r.sismember('set_name','aa'))

#有序集合操作
#增&改
r.zadd('zset_name','a1',6,'a2',2,'a3',5)
r.zadd('zset_name',a4=1,a5=2)
r.zincrby('zset_name','a1',amount=2)
#查
print(r.zcard('zset_name'))#元素数量
print(r.zcount('zset_name',1,5))#数值在区间的数量
#按索引取值，desc排序规则，score_cast_func数值处理函数
print(r.zrange("zset_name",0,1,desc=False,withscores=True,score_cast_func=int))
print(r.zscore("zset_name","a1"))
print(r.zrank("zset_name", "a1"))  #获取索引（从0开始）
print(r.zrevrank("zset_name", "a4"))#从大到小排序
#删
r.zrem("zset_name","a2","a5")
r.zremrangebyrank("zset_name", 3, 5)  #根据排行范围删除
r.zremrangebyscore("zset_name", 3, 5) #根据分数范围删除
r.zinterstore("zset_dest",("zset_name1","zset_name2"),aggregate="MAX")#交集放入新集


