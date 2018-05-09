import json
from utils.configStr import *
from utils.tools import *


class xpath(object):
    def __init__(self, json_data):
        self.title = json_data[TITLE]
        self.publishtime = json_data[PUBLISHTIME]
        self.content = json_data[CONTENT]
        self.link_list = json_data[LINK_LIST]
        self.source = json_data[SOURCE]
        self.cover = json_data[COVER]
        #self.is_group_link = json_data[IS_GROUP_LINKS]

    def get_title(self):
        return self.title

    def get_content(self):
        return self.content

    def get_publishtime(self):
        return self.publishtime

    def get_link_list(self):
        return self.link_list

    # def get_link(self):
    #     return self.link

    def get_source(self):
        return self.source

    def get_cover(self):
        return self.cover

    # def get_is_group_link(self):
    #     return self.is_group_link


class json2Dict(object):
    def __init__(self, json_data):
        super().__init__()
        #json_data = read_json(path)
        self.start_url = json_data[START_URL]
        self.allowed_domains = json_data[ALLOWED_DOMAINS]
        self.name = json_data[NAME]
        self.xpath = xpath(json_data[XPATH])

        # title = json_data[XPATH][TITLE]
        # publishtime = json_data[XPATH][publishtime]
        # content = json_data[XPATH][CONTENT]
        # cover = json_data[XPATH][COVER]

    def get_xpath(self):
        return self.xpath

    def __str__(self):
        return str(self.xpath)
        # if __name__=='__main__':
        #     json2XPath('./scrape_news/web_config/qq.json')
