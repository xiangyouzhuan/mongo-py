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

# condition = {'name': 'Jordan'}
# student = collection.find_one(condition)
# result = collection.update_one({'name': 'Jordan'},{"$set":{"age":22}})


def updateOne(filter,json):
    filter = eval(filter)
    json = '{"$set": ' + json + '}'
    json = eval(json)
    result = collection.update_many(filter, json)
    return result


