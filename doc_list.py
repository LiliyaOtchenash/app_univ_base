__author__ = 'a'

course1 = {'title': 'Python',
          'description': 'widely used general-purpose, high-level programming language'}
course2 = {'title': 'JavaScript',
           'description': 'high level, dynamic, untyped, and interpreted programming language'}
course3 = {'title': 'Java',
           'description': 'general-purpose computer programming language' }


teacher1 = {'first_name': 'Andrew', 'cource_id': course1.get('_id')}
teacher2 = {'first_name': 'Anton', 'cource_id': course2.get('_id')}
teacher3 = {'first_name': 'Ivan', 'cource_id': course3.get('_id')}


student1 = {'name': 'Liliya', 'sourname': 'Otchenash', 'groop': 1,
            'course_id': [course1.get('_id'), course2.get('_id')]}
student2 = {'name': 'Olga', 'sourname': 'Rudenko', 'groop': 2,
            'course_id': [course1.get('_id'), course3.get('_id')]}
student3 = {'name': 'Fill', 'sourname': 'Sharp', 'groop': 1,
            'course_id': [course2.get('_id'), course3.get('_id')]}



