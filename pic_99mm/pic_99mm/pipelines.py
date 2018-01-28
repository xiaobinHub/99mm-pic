# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class Pic99MmPipeline(object):
    def __init__(self):
        con = pymysql.connect(host="localhost", user="root", passwd="112233", db="xiaobin", charset="utf8mb4")
        cur = con.cursor()
        try:
            cur.execute(
                'create table 99mm_pic(编号 text(256), 标题 text(256), 链接 text(256)) engine=innodb charset=utf8mb4')
            con.commit()
            con.close()
        except:     
            con.close()
            pass
    
    def process_item(self, item, spider):
        title = item['title']
        pic_url = item['pic_url']
        pic_num = str(item['pic_num'])
        
        con = pymysql.connect(host="localhost", user="root", passwd="112233", db="xiaobin", charset="utf8mb4")
        cur = con.cursor()
        try:
            cur.execute("insert into 99mm_pic(编号,标题,链接) values ('{}','{}','{}')".format(pic_num,title,pic_url))
            con.commit()
            print('--[保存成功]-{}/{}'.format(title,pic_num))
        except:
            print('--[保存失败]-{}/{}'.format(title,pic_num))
            pass

        return item






        
