# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class LagouPipeline(object):
    def process_item(self, item, spider):
        title = item['title']
        address = item['address']
        money = item['money']
        company = item['company']
        fintance = item['fintance']

        # 和本地的scrapyDB数据库建立连接
        connection = pymysql.connect(
            host='localhost',  # 连接的是本地数据库
            user='root',        # 自己的mysql用户名
            passwd='password',  # 自己的密码
            db='test',      # 数据库的名字
            charset='utf8mb4',     # 默认的编码方式：
            cursorclass=pymysql.cursors.DictCursor)

        try:
            with connection.cursor() as cursor:
                # 创建更新值的sql语句

                # 执行sql语句
                # excute 的第二个参数可以将sql缺省语句补全，一般以元组的格式
                cursor.execute('INSERT INTO lagou(title,address,money,company,fintance)VALUES (%s,%s,%s,%s,%s)', (title,address,money,company,fintance))

            # 提交本次插入的记录
            connection.commit()
        finally:
            # 关闭连接
            connection.close()

        return item