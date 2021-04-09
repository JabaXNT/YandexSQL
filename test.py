from requests import get, delete, post

a = delete('http://localhost:5000/api/jobs/1').json()
print(a)
