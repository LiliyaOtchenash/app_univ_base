
from pymongo import MongoClient
from bson import ObjectId

client = MongoClient()
db = client.univ_database
db_teacher_first_name = db.teacher.find({}, {'first_name': 1, '_id': 0})

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--teachers', '-t', help='list of courses', action='store_true')
parser.add_argument('--courses', '-c', help='list of courses and teachers', action='store_true')
parser.add_argument('--student', '-s', help='list of courses, teachers and students', action='store_true')
parser.add_argument('--add_course', help='adding new course', action='store_true')
#parser.add_argument('title')
parser.add_argument('title_value')
#parser.add_argument('discr')
parser.add_argument('discr_value')

args = parser.parse_args()
#db.course.insert({'title': 'Python', 'description': 'widely used general-purpose, high-level programming language'})
#app.py --add_cource="строка в нужном для тебя формате чтобы создать новый курс"
#app.py --add-teache= "строка в нужном для тебя формате чтобы создать нового препода"
#app.py --add-student="строка в нужном для тебя формате чтобы создать нового препода"


if args.teachers:
    print('TEACHER NAME')
    for teacher in list(db_teacher_first_name):
        print(list(teacher.values())[0])

if args.courses:
    print('course name', 'teacher name')
    for teacher in db.teacher.find({}):
        cource = db.course.find_one({'_id': teacher.get('cource_id')})
        print(cource.get('title'), teacher.get('first_name'))



if args.student:
    print('student name', 'course name', 'teacher name')
    for student in db.student.find({}):
        a = student.get('course_id')
        for code in student.get('course_id'):
            cource = db.course.find_one({'_id': code})
            teacher = db.teacher.find_one({'cource_id': cource.get('_id')})
            print(student.get('name'), '--', cource.get('title'), '--', teacher.get('first_name'))



new_course = {'title': args.title_value, 'description': args.discr_value}
if args.add_course:
    a = db.course.find_one({'title': args.title_value})
    if a == None:
        db.course.insert(new_course)
        print('NEW DOCS ADDED', list(db.course.find({})))

    else:
        print('such course is already in the collection')
        print('ALL DOCS', list(db.course.find({})))

# {'title': 'C++', 'description': 'general-purpose programming language'}