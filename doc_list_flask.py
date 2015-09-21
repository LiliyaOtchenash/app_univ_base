from pymongo import MongoClient
from bson import ObjectId

client = MongoClient()
db = client.univ_database
db_teacher_first_name = db.teacher.find({}, {'first_name': 1, '_id': 0})

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--teachers', '-t', help='list of courses', action='store_true')
parser.add_argument('--courses', '-c', help='list of courses and teachers', action='store_true')
parser.add_argument('--students', '-s', help='list of courses, teachers and students', action='store_true')
parser.add_argument('--add_course', help='adding new course', nargs='*')
parser.add_argument('--add_teacher', help='adding new teacher', nargs=2)


args = parser.parse_args()

if args.teachers:
    print('TEACHER NAME')
    for teacher in list(db_teacher_first_name):
        print(list(teacher.values())[0])

if args.courses:
    print('course name', 'teacher name')
    for teacher in db.teacher.find({}):
        cource = db.course.find_one({'_id': teacher.get('cource_id')})
        print(cource.get('title'), teacher.get('first_name'))



if args.students:
    print('student name', 'course name', 'teacher name')
    for student in db.student.find({}):
        a = student.get('course_id')
        for code in student.get('course_id'):
            cource = db.course.find_one({'_id': code})
            teacher = db.teacher.find_one({'cource_id': cource.get('_id')})
            print(student.get('name'), '--', cource.get('title'), '--', teacher.get('first_name'))

