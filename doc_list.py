from pymongo import MongoClient
client = MongoClient()
db = client.univ_database
db_teacher_first_name = db.teacher.find({}, {'first_name': 1, '_id': 0})
db_course_title = db.course.find({}, {'title': 1, '_id': 0})


import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--teachers', '-t', help='list of courses', action='store_true')
parser.add_argument('--courses', '-c', help='list of courses and teachers', action='store_true')

args = parser.parse_args()

if args.teachers:
    print('TEACHER NAME')
    for teacher in list(db_teacher_first_name):
        print(list(teacher.values())[0])


if args.courses:
    print('course name', 'teacher name')
    for course in list(db_course_title):
        cors = list(course.values()[0]
        for teacher in list(db_teacher_first_name):
            print(cors, list(teacher.values())





print(cor)















#print(list(db.course.find()))
#print(list(db.teacher.find()))
#print(list(db.student.find()))
#db.teacher.find('null', {'first_name': 1, '_id': 0})  не сработало в Python, но работает в mongoShell




