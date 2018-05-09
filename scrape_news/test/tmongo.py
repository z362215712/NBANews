import re
from pymongo import MongoClient

mongo_server = "120.77.206.145"
mongo_port = 28888
mongo_db = "db_news"
mongo_col = "nba_news"

# client = MongoClient(mongo_server, mongo_port)
# db_auth = client['admin']
# db_auth.authenticate("vincent","qweqwe")
# db = client[mongo_db]
# db[mongo_col].insert(dict({"name":"yoga"}))


str = '2017年12月13日17:47'
# prog = re.compile("(\d+)年(\d+)月")
# result = prog.match(str)
result = re.findall('\d+',str)
print(result)
print()