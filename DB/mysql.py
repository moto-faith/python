import pymysql
# 数据库的连接
conn = pymysql.connect(host = '127.0.0.1',port = 3306, user = 'root', password = 'password', db = 'test')
# 创建操作的游标
cursor = conn.cursor()
# 编写sql语句
# 增
sql  = "insert into test_table(name, age, title, content) values('tom',22,'this is title', 'this is content')"
# 删
sql1 = "delete from test_table where id = 4"
# 查(需要fetch)
sql2 = "select * from test_table where id = 2"
# 改
sql3 = "update test_table set name = 'peter' where id = 2"
# 创建数据库
sql4 = "create database if not exists school"
# 删除数据库
sql5 = "drop database if exists school"
# 创建表
sql6 = "create table if not exists Student(Sno char(10)not null,Sname char(10),Ssex char(2),Sage int,Sdept varchar(20)) "
# 删除表
sql7 = "drop table if exists Student"
cursor.execute(sql)
conn.commit()
row = cursor.fetchone()
print(row)
