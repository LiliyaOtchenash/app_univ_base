from flask import Flask, url_for
app = Flask(__name__)
from doc_list import *

###################################################################
@app.route('/teachers')
def teachers():
    a = []
    for teacher in list(db_teacher_first_name):
        a.append(list(teacher.values()))
    return 'TEACHER NAMES {}'.format(a)
###################################################################
@app.route('/cources')
def cources():
    cour = []
    for course in db.course.find({}):
        cor = db.teacher.find_one({'cource_id': course.get('_id')})
        if cor:
            L = (course.get('title'), cor.get('first_name'))
            cour.append(L)
        else:
            K = (course.get('title'), '_no teacher_')
            cour.append(K)
    print(len(cour))
    return ("'course name', 'teacher name' {}".format(cour))
###################################################################
@app.route('/students')
def students():
    stud = []
    for student in db.student.find({}):
        a = student.get('course_id')
        for code in student.get('course_id'):
            cource = db.course.find_one({'_id': code})
            teacher = db.teacher.find_one({'cource_id': cource.get('_id')})
            S = (student.get('name'), cource.get('title'), teacher.get('first_name'))
            stud.append(S)
    return "'student name', 'course name', 'teacher name' {}".format(stud)



app.debug = True

if __name__ == '__main__':
    app.run()
