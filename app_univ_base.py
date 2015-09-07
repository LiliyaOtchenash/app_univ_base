from flask import Flask, url_for
app = Flask(__name__)
from doc_list_flask import *

@app.route('/course')
def courses():
    a = []
    for teacher in list(doc_list_flask.db_teacher_first_name):
        a.append(list(teacher.values()))
    return '%s, %s' % ('TEACHER NAMES', a)

@app.route('/courses')
def coursess():
    if args.students:

    return '%s, %s' % ('TEACHER NAMES', list(teacher.values())[0])



import doc_list_flask
@app.route('/teacher')
def hlello_world():
    return 'when this is called?'




app.debug = True

if __name__ == '__main__':
    app.run()
    print('app run called')









# http://127.0.0.1:5000/
# http://0.0.0.0:5000/
import doc_list_flask

print('TEACHER NAME')
a = []
for teacher in list(doc_list_flask.db_teacher_first_name):
    a.append(list(teacher.values()))
print(a)
