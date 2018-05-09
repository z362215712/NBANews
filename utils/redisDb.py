import redis
from scrapy.conf import settings


class RedisDb(object):
    def __init__(self):
        self.redis_db = redis.Redis(host=settings.get('REDIS_HOST'), port=settings.get('REDIS_PORT'),db=1,
                                    password=settings.get('REDIS_PASSWD'))
        self.url_uuid = "news_uuid"

    def sadd(self, col_name, value):
        return self.redis_db.sadd(col_name, value)

    def get_key_name(self):

        return self.url_uuid
