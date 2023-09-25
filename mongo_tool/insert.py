import pymongo
import json

# client = pymongo.MongoClient('mongodb://192.168.122.52:27017/')
client = pymongo.MongoClient(host='192.168.122.52',port=27017)
db = client['test']
collection = db['students']

def insertOne(file_data):
    with open(file_data, 'r') as file_js:
        file_data = file_js.read()
    print(file_data)
    print(type(file_data))
    file_data = eval(file_data)
    print(type(file_data))
    result = collection.insert_one(file_data)

# insertOne(student)


