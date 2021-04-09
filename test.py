from requests import get, delete, post

print(get('http://localhost:5000/api/news/1').json())

print(delete('http://localhost:5000/api/news/1').json())
# новости с id = 999 нет в базе