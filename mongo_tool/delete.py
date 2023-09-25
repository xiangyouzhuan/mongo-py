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


def deleteMany(filter):
    filter = eval(filter)
    exist = collection.find_one(filter)
    result = collection.delete_many(filter)
    return result

