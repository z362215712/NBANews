# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

# import sys
#
# sys.path.append('../')

import threading
from utils.tools import *
from scrapy.conf import settings
from pymongo import MongoClient
from utils.redisDb import RedisDb
import logging as log

Lock = threading.Lock()


class ScrapeNewsPipeline(object):
    def __init__(self, mongo_server, mongo_port, mongo_db, mongo_col):
        self.mongo_server = mongo_server
        self.mongo_port = mongo_port
        self.mongo_db = mongo_db
        self.mongo_col = mongo_col

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_server=crawler.settings.get('MONGODB_SERVER'),
            mongo_port=crawler.settings.get('MONGODB_PORT'),
            mongo_db=crawler.settings.get('MONGODB_DB'),
            mongo_col=crawler.settings.get('MONGODB_COL'),
        )

    def open_spider(self, spider):
        self.client = MongoClient(self.mongo_server, self.mongo_port)
        self.db_auth = self.client['admin']
        self.db_auth.authenticate("vincent","qweqwe")
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        redis = RedisDb()
        if redis.sadd(redis.get_key_name(), item['link']) == 1:
            self.db[self.mongo_col].insert(dict(item))
            #self.db[self.mongo_col].update({'link':item['link']},dict(item),True)
        else:
            log.info('已经爬过'+ item['link'])


    def close_spider(self, spider):
        self.client.close()

# if __name__ == '__main__':
#     item1 = ScrapeNewsPipeline()
#     item2 = ScrapeNewsPipeline()
#     print(item1)
#     print(item2)
