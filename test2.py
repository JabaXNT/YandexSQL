from requests import get, delete, post

a = delete('http://localhost:5000/api/jobs/6').json()
b = delete('http://localhost:5000/api/jobs/123').json()
c = delete('http://localhost:5000/api/jobs/qwe').json()

print(a, b, c, get('http://localhost:5000/api/jobs').json())