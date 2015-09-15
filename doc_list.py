from pymongo import MongoClient
from bson import ObjectId
import json
import argparse

client = MongoClient()
db = client.univ_database

parser = argparse.ArgumentParser()
parser.add_argument('--teachers', '-t', help='list of courses', action='store_true')
parser.add_argument('--courses', '-c', help='list of courses and teachers', action='store_true')
parser.add_argument('--students', '-s', help='list of courses, teachers and students', action='store_true')
parser.add_argument('--add_course', help='adding new course', nargs='*')
parser.add_argument('--add_teacher', help='adding new teacher', nargs='*')
parser.add_argument('--add_student', help='adding new teacher', nargs='*')



#a@a:~/dev/app_univ_base$
#--teachers

args = parser.parse_args()

def teach():
    print('TEACHER NAME')
    db_teacher_first_name = db.teacher.find({}, {'first_name': 1, '_id': 0})
    for teacher in list(db_teacher_first_name):
        print(list(teacher.values())[0])

def cours():
    print('course name', 'teacher name')
    for course in db.course.find({}):
        cor = db.teacher.find_one({'cource_id': course.get('_id')})
        if cor:
            print(course.get('title'), "_", cor.get('first_name'), '_')
        else:
            print(course.get('title'), '_no teacher_')

def studen():
    print('student name', 'course name', 'teacher name')
    for student in db.student.find({}):
        a = student.get('course_id')
        for code in student.get('course_id'):
            cource = db.course.find_one({'_id': code})
            teacher = db.teacher.find_one({'cource_id': cource.get('_id')})
            print(student.get('name'), '--', cource.get('title'), '--', teacher.get('first_name'))



# --add_course="{'title': 'C++', 'description': 'general-purpose programming language'}"
def add_cour():
    new_course_str = args.add_course[0]
    new_course = json.loads(new_course_str.replace("'", "\""))
    if list(sorted(new_course.keys())) == ['description', 'title']:
        new_course_for_add = db.course.find_one({'title': new_course.get('title')})
        if new_course_for_add == None:
            db.course.insert(new_course)
            print('NEW DOCS ADDED', list(db.course.find({})))
        else:
            print('such course is already in the collection')
            print('ALL DOCS', list(db.course.find({})))
    else:
        print('ITS WRONG GROOP OF KEYS Plese write string useing next pattern', ':', "{'title': 'C++', 'description': 'general-purpose programming language'}")

# --add_teacher="{'first_name': 'Fil', 'cource_id': '55e5b4c40cc17563d0f1c6a7'}"
def add_teach():
    new_teacher_str = args.add_teacher[0]
    new_teacher = json.loads(new_teacher_str.replace("'", "\""))
    if list(sorted(new_teacher.keys())) == ['cource_id', 'first_name']:
        new_teacher_for_add = db.teacher.find_one({'first_name': new_teacher.get('first_name')})
        if new_teacher_for_add == None:
            teach_id = ObjectId(new_teacher.get('cource_id'))
            new_teacher['cource_id'] = teach_id
            db.teacher.insert(new_teacher)
            print('NEW teacher ADDED', list(db.teacher.find({})))
        else:
            print('such teacher is already in the collection')
            print('ALL DOCS', list(db.teacher.find({})))
    else:
        print('Plese write string useing next pattern', ':', "{'first_name': 'Fil', 'cource_id': '55e5b4c40cc17563d0f1c6a7'}")

#--add_student="{'name' : 'Liliya', 'sourname' : 'Otchenash', 'groop' : 1, 'course_id' : ['55e41918fe9d5908f16b8e46', '55e41acb5ac9452058d01755']}"
def add_stud():
    new_student_str = args.add_student[0]
    new_student = json.loads(new_student_str.replace("'", "\""))
    list(sorted(new_student.keys()))
    if list(sorted(new_student.keys())) == ['course_id', 'groop', 'name', 'sourname']:
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
    else:
        print('Plese write string useing next pattern', "{'name': '......', 'sourname': '........', 'groop': .... , 'course_id': [........]}")


if __name__ == '__main__':

    if args.teachers:
        teach()
    elif args.courses:
        cours()
    elif args.students:
        studen()

    elif args.add_course:
        try:
            add_cour()
        except ValueError:
             print('WRONG DATA TYPE, please use next pattern', "{'title': 'C++', 'description': 'general-purpose programming language'}")


        #if args.add_course[0] == '':
         #   print(' ITS EMPTY STRING Plese write string useing next pattern', ':', "{'title': '......course_name.......', 'description': '....course_description....'}")
        #else:
         #   new_course_str = args.add_course[0]
          #  new_course = json.loads(new_course_str.replace("'", "\""))
           # if type(new_course) != type({}):
            #    print(' ITS NOT DICT Plese write string useing next pattern')
            #else:
             #   add_cour()

    elif args.add_teacher:
        try:
            add_teach()
        except ValueError:
            print('WRONG DATA TYPE, please use next pattern', "{'first_name': 'Fil', 'cource_id': '55e5b4c40cc17563d0f1c6a7'}")


    elif args.add_student:
        try:
            add_stud()
        except ValueError:
            print('WRONG DATA TYPE, please use next pattern', "{'name' : 'Liliya', 'sourname' : 'Otchenash', 'groop' : 1, 'course_id' : ['55e41918fe9d5908f16b8e46', '55e41acb5ac9452058d01755']}")

    else:
        print('Please, use one of special args')