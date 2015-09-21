__author__ = 'a'
from pymongo import MongoClient
client = MongoClient()
db = client.univ_database


#db.course.insert({'title': 'Python', 'description': 'widely used general-purpose, high-level programming language'})
#db.course.insert({'title': 'JavaScript', 'description': 'high level, dynamic, untyped, and interpreted programming language'})
#db.course.insert({'title': 'Java', 'description': 'general-purpose computer programming language'})
######

#db.course.insert({'title': 'C++', 'description': 'general-purpose programming language'})
#db.course.insert({'title': 'C#', 'description': ' multi-paradigm programming language'})

######
#db.teacher.insert({'first_name': 'Andrew', 'cource_id': ObjectId("55e41918fe9d5908f16b8e46")})
#db.teacher.insert({'first_name': 'Anton', 'cource_id': ObjectId("55e41acb5ac9452058d01755")})
#db.teacher.insert({'first_name': 'Ivan', 'cource_id': ObjectId("55e41b735ac9452058d01757")})
#####
{'first_name': 'Fil', 'cource_id': '55e5b4c40cc17563d0f1c6a7'}


#####
#db.student.insert({'name': 'Liliya', 'sourname': 'Otchenash', 'groop': 1, 'course_id': [ObjectId("55e41918fe9d5908f16b8e46"), ObjectId("55e41acb5ac9452058d01755")] })
#db.student.insert({'name': 'Olga', 'sourname': 'Rudenko', 'groop': 2, 'course_id': [ObjectId("55e41918fe9d5908f16b8e46"), ObjectId("55e41b735ac9452058d01757")] })
#db.student.insert({'name': 'Fill', 'sourname': 'Sharp', 'groop': 1, 'course_id': [ObjectId("55e41acb5ac9452058d01755")]})
######db.student.insert({'name': 'Stepa', 'sourname': 'Stepanov', 'groop': 1, 'course_id': [ObjectId("55e41acb5ac9452058d01755")]})
######db.student.insert({'name': 'Vova', 'sourname': 'Vovochkin', 'groop': 2, 'course_id': [ObjectId("55e41acb5ac9452058d01755")]})


> db.teacher.find({}, {first_name: 1, _id: 0})
> db.teacher.find(null, {first_name: 1, _id: 0})
{ "first_name" : "Andrew" }
{ "first_name" : "Ivan" }
{ "first_name" : "Anton" }


db.course.find({})
{ "_id" : ObjectId("55e41918fe9d5908f16b8e46"), "title" : "Python", "description" : "widely used general-purpose, high-level programming language" }
{ "_id" : ObjectId("55e41acb5ac9452058d01755"), "title" : "JavaScript", "description" : "high level, dynamic, untyped, and interpreted programming language" }
{ "_id" : ObjectId("55e41b735ac9452058d01757"), "title" : "Java", "description" : "general-purpose computer programming language" }
{'description': 'general-purpose programming language', 'title': 'C++', '_id': ObjectId('55e5b4c40cc17563d0f1c6a7')}
{'description': 'multi-paradigm programming language', 'title': 'C#', '_id': ObjectId('55e9ec5f0cc1753cecf80893')}


>
teacher
{ "_id" : ObjectId("55e41a745ac9452058d01754"), "first_name" : "Andrew", "cource_id" : ObjectId("55e41918fe9d5908f16b8e46") }
{ "_id" : ObjectId("55e41baa5ac9452058d01758"), "first_name" : "Ivan", "cource_id" : ObjectId("55e41b735ac9452058d01757") }
{ "_id" : ObjectId("55e41c6c5ac9452058d01759"), "first_name" : "Anton", "cource_id" : ObjectId("55e41acb5ac9452058d01755") }
>
student
> db.student.find()
{ "_id" : ObjectId("55e41f275ac9452058d0175a"), "name" : "Liliya", "sourname" : "Otchenash", "groop" : 1, "course_id" : [ ObjectId("55e41918fe9d5908f16b8e46"), ObjectId("55e41acb5ac9452058d01755") ] }
{ "_id" : ObjectId("55e41fde5ac9452058d0175b"), "name" : "Olga", "sourname" : "Rudenko", "groop" : 2, "course_id" : [ ObjectId("55e41918fe9d5908f16b8e46"), ObjectId("55e41b735ac9452058d01757") ] }
{ "_id" : ObjectId("55e4201b5ac9452058d0175c"), "name" : "Fill", "sourname" : "Sharp", "groop" : 1, "course_id" : ObjectId("55e41acb5ac9452058d01755") }






