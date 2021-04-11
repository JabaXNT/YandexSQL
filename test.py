from requests import get, delete, post, put


a = post('http://localhost:5000/api/v2/users/3',
        json={
            'team_leader': 3,
            'job': 'азазазаз',
            'work_size': 123,
            'collaborators': '2, 3',
            'is_finished': False, }).json()
d = delete('http://localhost:5000/api/v2/users/8').json()
b = post('http://localhost:5000/api/v2/users',
         json={'id': 8,
               'team_leader': 3,
               'job': 'азазазаз',
               'work_size': 123,
               'collaborators': '2, 3',
               'is_finished': False, }).json()
c = get('http://localhost:5000/api/v2/users').json()
e = get('http://localhost:5000/api/v2/jobs/users').json()
print(a, b, c, d, e)
