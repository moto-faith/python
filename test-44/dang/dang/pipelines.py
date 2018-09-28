# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class DangPipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='password', db='test')
        cursor = conn.cursor()
        for i in range(len(item['name'])):
            print(item['name'][i])
            print(item['num'][i])
            print(item['price'][i].encode('utf-8'))
            sql = "insert into book(name, num, price) values('"+item['name'][i]+"','"+item['num'][i]+"','"+item['price'][i]+"')"
            cursor.execute(sql)
            conn.commit()


        return item
