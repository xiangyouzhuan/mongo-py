import pymongo
from happy_python import HappyLog
from happy_python.happy_log import HappyLogLevel

client = pymongo.MongoClient()
db = client['test']
collection = db['students']
result = collection.find({})
collection.find_one()


print(result)
