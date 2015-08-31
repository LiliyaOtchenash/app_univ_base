from pymongo import MongoClient
client = MongoClient()
db = client.univ_database


for docs in db.collection_course.find():
    print('list of docs', docs)

print('1', list(db.collection_teachern_.find()))

print(db.collection_names(include_system_collections=False))
print(db)
print(db.collection_student.find_one())