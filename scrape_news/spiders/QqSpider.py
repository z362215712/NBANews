# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrape_news.spiders.CommonSpider import CommonSpider
from utils.tools import *

class QqSpider(CommonSpider):
    name = 'QqSpider'
    config_path='web_config/qq.json'

    def __init__(self):
        self.config = read_json(self.config_path)
        print(self.config)
        super().__init__(config=self.config)

