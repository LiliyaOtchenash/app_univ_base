from pymongo import MongoClient
client = MongoClient()
db = client.univ_database

collection_student = db.collection_student
Liliya = {'name': 'Liliya', 'sourname': 'Otchenash', 'age': 27, 'groop': 1, 'specialty': 'web-development', 'course': 'Python'}
collection_student_id = collection_student.insert_one(Liliya).inserted_id  ###  create id
print(collection_student_id)


collection_teacher = db.collection_teacher
Andrew = {'name': 'Andrew', 'sourname': 'Pogrebnjak', 'age': 27, 'experience': '10_years', 'teacher_direction': 'web-development', 'course': ['Python', 'JScript']}
collection_teacher_id = collection_teacher.insert_one(Andrew).inserted_id ###
print(collection_teacher_id)


collection_course = db.collection_course
Pythons = {'name': 'Pythons', 'last_version': '3.4', 'course_duration': '6_month', 'teacher': 'Andrew'}
collection_course_id = collection_course.insert_one(Pythons).inserted_id
print(collection_course_id)
Jscript = {'name': 'JScript', 'last_version': '5.4', 'course_duration': '2_month', 'teacher': 'Andrew'}
db.collection_course.save(Jscript)

for docs in db.collection_course.find():
    print('list of docs', docs)



print(db.collection_names(include_system_collections=False))
print(db)
print(db.collection_student.find_one())