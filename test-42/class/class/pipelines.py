# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ClassPipeline(object):
    def __init__(self):
        self.f = open('course.txt','a')
    def process_item(self, item, spider):
        print(item['name'])
        print(item['url'][0])
        print(item['num'])
        self.f.write(item['name']+'\n'+item['url'][0]+'\n'+item['num']+'\n'+'\n'+'\n')
        return item
    def close_spider(self):
        self.f.close()

