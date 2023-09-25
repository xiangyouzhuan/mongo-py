import pymongo

client = pymongo.MongoClient('mongodb://192.168.122.52:27017/')
db = client['test']
collection = db['students']

student = {
    'id': '20170101',
    'name': 'Jordan',
    'age': 20,
    'gender': 'male'
}

condition = {'name': 'Jordan'}
student = collection.find_one(condition)
result = collection.update_one(condition,{"$set":{"age":21}})
print(result)

