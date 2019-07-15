# _*_ coding: utf-8 _*_
__author__ = "吴飞鸿"
__date__ = "2019/7/15 23:17"

import pymongo
from pymongo.collection import Collection


class Connect_mongo(object):
    def __init__(self):
        # 客户端连接本地，并创建数据库
        self.client = pymongo.MongoClient(host='127.0.0.1')
        self.db_data = self.client['dou_guo_mei_shi']

    def insert_item(self, item):
        db_collection = Collection(self.db_data, 'dou_guo_mei_shi_item')
        db_collection.insert(item)


# 创建实例
mongo_info = Connect_mongo()