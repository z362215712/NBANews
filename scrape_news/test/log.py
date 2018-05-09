# import sys
# sys.path.append('../')
# # from utils.tools import *
# # from utils.json2Dict import *
# # import json
# import logging
#
# def log(LEVEL=logging.INFO):
#     #logging.basicConfig(level=logging.INFO)
#     logger = logging.getLogger(__name__)
#     logger.setLevel(logging.INFO)
#
#
#
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)
#
# logging.info('halo')

import os
import logging.config
import yaml
import sys

def setup_logging(
        default_path='../server_config/log.yaml',
        default_level=logging.INFO,
        env_key='LOG_CFG'
):
    """Setup logging configuration
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)


def get_logger(path):
    setup_logging(default_path=path)
    return logging.getLogger('loggers')




