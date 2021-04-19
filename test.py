from requests import get, delete, post, put


a = put('http://localhost:5000/api/v2/users/2',
         json={
             'surname': 'Ridley',
             'name': "Scott",
             'age': 25,
             'position': 'chief',
             'speciality': 'senior engineer',
             'address': 'module_1',
             'email': 'scott_chie@mars.org',
             'hashed_password': '456', }).json()
print(a)
