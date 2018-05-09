import sys
sys.path.append('../')
sys.path.append('../../')
from utils.tools import *
from utils.json2Dict import *
from  utils.log import *
import json
import logging


logger = get_logger()
logger.info('this is a test')



# config_path = '../web_config/zhiboba.json'
# start_url = 'GET /interface/tag/articles.php?callback=tagListCb&p=1&l=20&tag=NBA&oe=gbk&ie=utf-8&source=web&site=sports&_=1512093187708'
#
# config = read_json(config_path)
# print(config)
#
# data = json2Dict(config)
# print(data)
# print(data.get_xpath())
# print(data.get_xpath().get_link())
# print(data.get_xpath().get_article_list())



# for (index,item) in config.items():
#     print(index)
#     print(item)
#
# print(config['name'])
# print(config['xpath']['source'])


