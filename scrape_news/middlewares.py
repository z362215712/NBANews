# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import requests
from bs4 import BeautifulSoup
import logging as log
from scrapy.exceptions import IgnoreRequest
from fake_useragent import UserAgent
import time


class ScrapeNewsSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class CustomDownloaderMiddleware(object):
    def process_request(self, spider, request):
        ## PhantomJS
        proxy = self.get_random_proxy()
        request.meta["proxy"] = proxy
        request.meta['headers']= self.get_headers()

    def process_response(self, request, response, spider):
        # 对返回的response处理
        # 如果返回的response状态不是200，重新生成当前request对象
        if response.status != 200:
            proxy = self.get_random_proxy()
            # 对当前reque加上代理
            request.meta['proxy'] = proxy
            request.meta['headers']= self.get_headers()
            return request
        return response

    def get_random_proxy(self):
        '''获取代理IP地址'''
        try:
            content = requests.get('http://0.0.0.0:5555/random')
            if content is None:
                return self.get_random_proxy()
            proxy = BeautifulSoup(content.text, 'lxml').get_text()
            time.sleep(1)
            print("IP地址："+proxy)
            return 'http://' + proxy
        except:
            return self.get_random_proxy()

    def get_headers(self):
        ua = UserAgent()
        base_headers = {
            'User-Agent': ua.random,
            'Accept-Encoding': 'gzip, deflate, sdch',
            'Accept-Language': 'zh-CN,zh;q=0.8'
        }
        headers = dict(base_headers)
        print('请求头')
        print(headers)
        return headers
