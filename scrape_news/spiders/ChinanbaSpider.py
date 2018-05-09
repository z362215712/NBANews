# -*- coding: utf-8 -*-
import scrapy
from scrape_news.spiders.CommonSpider import CommonSpider
from utils.tools import *


class ChinanbaSpider(CommonSpider):
    name = 'ChinanbaSpider'
    config_path ='./web_config/chinanba.json'

    def __init__(self):
        self.config = read_json(self.config_path)

        # if self.config.__contains__('start_url') == False:
        #     self.config['start_url'] = self.start_url
        print(self.config)
        super().__init__(config=self.config)
