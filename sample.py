import pymongo

__author__ = 'a'


connection = pymongo.MongoClient()
db = connection.sample_db
doc = {'title': 'some text'}
def create_doc():
    db.test_collection.insert_one(doc)
print(doc)
doc['title'] = 'nww text'
#db.test_collection.replace_one({'_id': doc['_id']}, doc)
#print(doc)
#print(list(db.test_collection.find({})))

docx = {'titlex': 'some textx'}
db.test_collection.save(docx)
print(list(db.test_collection.find({})))

