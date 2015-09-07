from pymongo import MongoClient
from bson import ObjectId
import json

client = MongoClient()
db = client.univ_database
db_teacher_first_name = db.teacher.find({}, {'first_name': 1, '_id': 0})

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--teachers', '-t', help='list of courses', action='store_true')
parser.add_argument('--courses', '-c', help='list of courses and teachers', action='store_true')
parser.add_argument('--courses_new', '-n', help='list of courses and teachers', action='store_true')

parser.add_argument('--students', '-s', help='list of courses, teachers and students', action='store_true')
parser.add_argument('--add_course', help='adding new course', nargs='*')
parser.add_argument('--add_teacher', help='adding new teacher', nargs='*')
parser.add_argument('--add_student', help='adding new teacher', nargs='*')

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
    for course in db.course.find({}):
        cor = db.teacher.find_one({'cource_id': course.get('_id')})
        if cor:
            print(course.get('title'), "_", cor.get('first_name'), '_')
        else:
            print(course.get('title'), '_no teacher_')


if args.courses_new:
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


if args.add_course:
    new_course_str = args.add_course[0]
    new_course = json.loads(new_course_str.replace("'", "\""))
    new_course_for_add = db.course.find_one({'title': new_course.get('title')})
    if new_course_for_add == None:
        db.course.insert(new_course)
        print('NEW DOCS ADDED', list(db.course.find({})))
    else:
        print('such course is already in the collection')
        print('ALL DOCS', list(db.course.find({})))


if args.add_teacher:
    new_teacher_str = args.add_teacher[0]
    new_teacher = json.loads(new_teacher_str.replace("'", "\""))
    new_teacher_for_add = db.teacher.find_one({'first_name': new_teacher.get('first_name')})
    if new_teacher_for_add == None:
        teach_id = ObjectId(new_teacher.get('cource_id'))
        new_teacher['cource_id'] = teach_id
        db.teacher.insert(new_teacher)
        print('NEW teacher ADDED', list(db.teacher.find({})))
    else:
        print('such teacher is already in the collection')
        print('ALL DOCS', list(db.teacher.find({})))

if args.add_student:
    new_student_str = args.add_student[0]
    new_student = json.loads(new_student_str.replace("'", "\""))
    new_student.get('course_id')

    new_student_for_add = db.student.find_one({'name': new_student.get('name')})
    stud_id = ObjectId(new_student.get('cource_id'))


    if new_student_for_add == None:
        course_ids = []
        for st in new_student.get('course_id'):
            course_ids.append(ObjectId(st))
        new_student['course_id'] = course_ids
        db.student.insert(new_student)
        print('NEW student ADDED', list(db.student.find({})))
    else:
        print('such student is already in the collection')
        print('ALL DOCS', list(db.student.find({})))







