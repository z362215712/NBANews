# -*- coding: utf-8 -*-

from scrape_news.spiders.CommonSpider import CommonSpider
from utils.tools import *

class SinaSpider(CommonSpider):
    name = 'SinaSpider'
    config_path='./web_config/sina.json'

    def __init__(self):
        self.config = read_json(self.config_path)
        print(self.config)
        super().__init__(config=self.config)

