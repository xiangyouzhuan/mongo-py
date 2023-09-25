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

def insertOne(file_data):
    with open(file_data, 'r') as file_js:
        file_data = file_js.read()
    print(file_data)
    # print(type(file_data))
    file_data = eval(file_data)
    # print(type(file_data))
    result = collection.insert_one(file_data)
    return result


