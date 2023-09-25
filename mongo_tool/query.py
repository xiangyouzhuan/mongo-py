import configparser
from pathlib import Path
import pymongo

conf_dir = Path(__file__).parent.parent / 'conf'
app_conf_file = conf_dir / 'config.ini'
cfg = configparser.ConfigParser()
cfg.read(app_conf_file)
ip = cfg['mongo']['ip']
port = int(cfg['mongo']['port'])

client = pymongo.MongoClient(host=ip, port=port)
db = client['test']
collection = db['students']


def query(filter):
    # cursor = collection.find({"age": {"$gt": 18}})
    filter = eval(filter)
    cursor = collection.find(filter)
    return cursor
