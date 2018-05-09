# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.spiders import CrawlSpider
from scrape_news.items import ScrapeNewsItem

from utils.json2Dict import xpath, json2Dict
from utils.configStr import *
import datetime


class CommonSpider(CrawlSpider):
    name = 'CommonSpider'

    def __init__(self, **kwargs):
        config_path = kwargs['config']
        self.data = json2Dict(config_path)

    def start_requests(self):
        yield scrapy.Request(url=self.data.start_url, callback=self.parse_item,dont_filter=True)
        # yield scrapy.Request(url='http://nbachina.qq.com/a/20171206/033969.htm', callback=self.parse_detail)


    def parse_item(self, response):
        xpath = self.data.get_xpath()
        link_list = response.xpath(xpath.get_link_list()).extract()

        for link in link_list:
            if re.match("http",link) is None:
                link = response.urljoin(link)
                print(link)
            yield scrapy.Request(url=link, callback=self.parse_detail)



    def parse_detail(self, response):
        print("结果是：")
        print(response)
        print(self.data.get_xpath())

        xpath = self.data.get_xpath()
        print(response.xpath(xpath.get_title()).extract_first().strip())
        now = datetime.datetime.now()
        item = ScrapeNewsItem()
        item[LINK] = response.url
        item[TITLE] = response.xpath(xpath.get_title()).extract_first().strip()
        item[SOURCE] = response.xpath(xpath.get_source()).extract_first()
        item[ADDTIME] =now.strftime('%Y-%m-%d %H:%M:%S')
        publish_time = response.xpath(xpath.get_publishtime()).extract_first().strip()
        if '年' in publish_time:
            publish_time = re.findall("\d+",publish_time)
            item[PUBLISHTIME] ="{0}-{1}-{2} {3}:{4}".format(publish_time[0],publish_time[1],publish_time[2],publish_time[3],publish_time[4])
        else:
            item[PUBLISHTIME] = publish_time
        item[COVER] = response.xpath(xpath.get_cover()).extract_first()

        content_list = response.xpath(xpath.get_content()).extract()
        str = ''
        for p in content_list:
            str = str + p

        item[CONTENT] = str

        yield item
