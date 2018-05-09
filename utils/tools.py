import time
import json
import logging
import os
import yaml
from utils.log import *


logger = get_logger()

def get_timestamp():
    t = time.time()
    nowTime = lambda: int(round(t * 1000))
    print(nowTime());  # 毫秒级时间戳，基于lambda


def read_json(path):
    try:
        with open(path) as f:
            data = json.load(f)
        return data
    except OSError as e:
        print(e)


def write_json( path, data):
    try:
        with open(path, 'w+') as f:
            json.dump(data, f)
    except OSError as e:
        print(e)


def read_yaml(path):
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.load(f.read())
        return config
    else:
        logger.error("file not exist:%s",path)
        return False

