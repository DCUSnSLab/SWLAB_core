import requests

url = 'http://localhost:8000/api/logintest'
data = {'username':'test',
        'password':'12341234'}

session = requests.Session()
print(session.cookies.set_cookie())
http_post_request = session.post(url, json=data)
print(http_post_request.text)