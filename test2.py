from requests import get, delete, post, put


a = post('http://localhost:5000/api/v2/users/2',
         json={
             'surname': 'Ridley',
             'name': "Scott",
             'age': 25,
             'position': 'chief',
             'speciality': 'senior engineer',
             'address': 'module_1',
             'email': 'scott_chie@mars.org',
             'hashed_password': '456', }).json()
d = delete('http://localhost:5000/api/v2/users/5').json()
b = post('http://localhost:5000/api/v2/users',
         json={
             'surname': 'Test1',
             'name': "Test2",
             'age': 30,
             'position': 'SD',
             'speciality': 'senior developer',
             'address': 'module_3',
             'email': 'test@mars.org',
             'hashed_password': '789', }).json()
c = get('http://localhost:5000/api/v2/users').json()
e = get('http://localhost:5000/api/v2/users/1').json()
print(a, b, c, d, e)
