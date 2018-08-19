import numpy as np
a=np.arange(10)

b=a.reshape(2,5)

c=np.arange(24).reshape(2,3,4)

e=np.array([1,2,3])
f=np.array([[1,2,3],[4,5,6]])

a=np.zeros(5)

a=np.arange(10)
a[5]=100
a[1:4]=100

a=np.random.rand(3,4)

# print(np.zeros([2,4]))
# print(np.ones([2,4]))
# print(np.random.rand(2,4))
# print(np.random.randint(1,10,5))
# print(np.random.randn(2,4))
# print(np.random.choice([10,20,30]))

a=np.random.normal(size=(3,4))

a=np.random.randint(1,5,(3,4))
# print(a.T)

# print(np.sqrt(a))

s=np.random.randn(2,3)
# print(np.sum(s))

a1=np.arange(10,0,-1).reshape(2,5)
b1=np.arange(10).reshape(2,5)
# print(np.maximum(a1,b1))


s=np.arange(1,25).reshape(3,2,4)
# print(s.sum(axis=2))

# print(np.cumsum(a1))
# print(np.cumprod(a1))

c1 = np.array([True,True,True,False,False,False])
# print(np.cumsum(c1))
d=np.random.rand(2,5)
# print(np.sort(d))

cond =  np.array([True,False,True,False])
x= np.array([1,2,3,4])
y=np.array([5,6,7,8])
e=np.where(cond,x,y)
# print(e)

# print(np.unique(a))
# print(np.max(a))
# print(np.min(a))
np.save('study',a)
print(np.load('study.npy'))









