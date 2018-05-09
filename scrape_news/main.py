import sys
sys.path.append('../')
from utils.tools import *
from utils.log import *
import os
import time

logger = get_logger()

def get_spider_list():
    path='./server_config/spider_list.json'
    lst = read_json(path)
    items = lst['list']
    return [item for item in items]

def do_scrape_task():
    lst = get_spider_list()
    for spider_name in lst:
        logger.info(" Starting crawl %s",spider_name)
        os.system("scrapy crawl %s"%spider_name)



def run():
    while True:
        config_path = './server_config/run.yaml'
        config = read_yaml(config_path)
        minutes = config['minutes']
        do_scrape_task()
        logger.warn('scrape all, now sleeping %d minutes' % minutes)
        time.sleep(minutes)


if __name__=='__main__':
    spider_lst=  do_scrape_task()

