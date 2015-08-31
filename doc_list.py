__author__ = 'a'
from pymongo import MongoClient
client = MongoClient()
db = client.univ_database

print(list(db.course.find()))
print(list(db.teacher.find()))
print(list(db.student.find()))



db_teacher_first_name = db.teacher.find({}, {'first_name': 1, '_id': 0})
print('TEACHER NAME')
for teacher in list(db_teacher_first_name):
    #print('TEACHERS: ', teacher)
    print(list(teacher.values()))



#db.teacher.find('null', {'first_name': 1, '_id': 0})




