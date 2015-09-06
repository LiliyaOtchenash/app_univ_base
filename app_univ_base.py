from flask import Flask, url_for
app = Flask(__name__)
import doc_list_flask

@app.route('/course')
def hello_world():
    print('when this is called?')
    a = []
    for teacher in list(doc_list_flask.db_teacher_first_name):
        a.append(list(teacher.values()))
    return '%s, %s' % ('TEACHER NAMES', a)

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
