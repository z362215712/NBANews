# -*- coding: utf-8 -*-
import scrapy
from scrape_news.spiders.CommonSpider import CommonSpider
from scrapy.selector import HtmlXPathSelector
from utils.tools import *
import time
import datetime

class ZhibobaSpider(CommonSpider):
    name = 'ZhibobaSpider'
    config_path='./web_config/zhiboba.json'
    start_url = 'GET /interface/tag/articles.php?callback=tagListCb&p=1&l=20&tag=NBA&oe=gbk&ie=utf-8&source=web&site=sports&_=1525791433'

    def __init__(self):
        self.config = read_json(self.config_path)
        print("__________________________________")
        print(self.config)
        super().__init__(config=self.config)

