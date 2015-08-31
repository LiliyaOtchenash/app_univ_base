from pymongo import MongoClient
client = MongoClient()
db = client.univ_database
db_teacher_first_name = db.teacher.find({}, {'first_name': 1, '_id': 0})

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--courses', '-c', help='list of courses', action='store_true')
args = parser.parse_args()

if args.courses:
    print('TEACHER NAME')
    for teacher in list(db_teacher_first_name):
        print(list(teacher.values()))



#print(list(db.course.find()))
#print(list(db.teacher.find()))
#print(list(db.student.find()))
#db.teacher.find('null', {'first_name': 1, '_id': 0})  не сработало в Python, но работает в mongoShell




