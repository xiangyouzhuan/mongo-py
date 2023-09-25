import pymongo

client = pymongo.MongoClient('mongodb://192.168.122.52:27017/')
db = client['test']
collection = db['students']

student = {
    'id': '20170102',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

result = collection.delete_one({'id':'20170102'})
# result = collection.count_documents({})
print(result)

