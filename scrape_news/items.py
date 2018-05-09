# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapeNewsItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    link = scrapy.Field()
    addtime = scrapy.Field()
    cover = scrapy.Field()
    content = scrapy.Field()
    source = scrapy.Field()
    publishtime = scrapy.Field()

