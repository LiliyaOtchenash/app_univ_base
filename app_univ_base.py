from flask import Flask
from doc_list import db_teacher_first_name
from flask import render_template
import jinja2
ap = Flask(__name__)
from doc_list import *
ap.debug = True
###################################################################
@ap.route('/teachers')
def teacher_list():
    user = {'hat_of_table': 'TEACHER NAMES'}
    posts = list(db_teacher_first_name)
    return render_template('teachers.html',
                           title = 'teachers',
                           user = user,
                           posts = posts)
###################################################################
@ap.route('/cources')
def cources():
    title = 'cources'
    user = {'hat_of_table': 'Course Name, Teacher Name'}
    cour = []
    for course in db.course.find({}):
        cor = db.teacher.find_one({'cource_id': course.get('_id')})
        if cor:
            L = (course.get('title'), course.get('_id'), cor.get('first_name'))
            cour.append(L)
        else:
            K = (course.get('title'),  course.get('_id'), '_no teacher_')
            cour.append(K)
    #print(len(cour))
    return render_template('cources.html',
                           title = title,
                           user = user,
                           cour = cour)


###################################################################
@ap.route('/students')
def students():
    title = 'students'
    user = {'hat_of_table': 'Student Name, Course Name, Teacher Name'}
    stud = []
    for student in db.student.find({}):
        a = student.get('course_id')
        for code in student.get('course_id'):
            cource = db.course.find_one({'_id': code})
            teacher = db.teacher.find_one({'cource_id': cource.get('_id')})
            S = (student.get('name'), cource.get('title'), teacher.get('first_name'))
            stud.append(S)
    return render_template('students.html',
                           title = title,
                           user = user,
                           stud = stud)



if __name__ == '__main__':
    ap.run()




###################################################################
#@app.route('/teachers')
#def teachers():
 #   a = []
  #  for teacher in list(db_teacher_first_name):
   #     a.append(list(teacher.values()))
    #return 'TEACHER NAMES {}'.format(a)
