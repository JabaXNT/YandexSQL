from requests import get, delete, post


a = post('http://localhost:5000/api/jobs',
         json={'id': 6,
               'team_leader': 3,
               'job': 'азазазаз',
               'work_size': 123,
               'collaborators': '2, 3',
               'is_finished': False, }).json()
b = post('http://localhost:5000/api/jobs',
         json={'id': 6,  # Id совпадает с тем что уже в бд
               'team_leader': 2,
               'job': 'Бессмысленный текст',
               'work_size': 12,
               'collaborators': '2, 3, 4',
               'is_finished': False, }).json()
c = post('http://localhost:5000/api/jobs',
         json={'id': 9,
               'job': 'азазазаз',
               'work_size': 123,
               'collaborators': '2, 3',
               'is_finished': False, }).json()  # не хватает столбца Team_leader
d = post('http://localhost:5000/api/jobs',
         json={'id': 10,
               'team_leader': 3,
               'job': '123',
               'work_size': 123,
               'collaborators': '2, 3',
               'is_finished': 3, }).json()  # is_finished принимает только True, False и None
print(a, b, c, d, get('http://localhost:5000/api/jobs').json())
