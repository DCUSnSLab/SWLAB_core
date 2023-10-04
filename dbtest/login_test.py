import requests

url = 'http://localhost:8000/api/login'
data = {'username':'test',
        'password':'12341234'}

session = requests.Session()

http_post_request = session.post(url, json=data)
print(http_post_request.text)
print(http_post_request.cookies)

url = 'http://localhost:8000/api/logintest'
data = {'username':'test',
        'password':'12341234'}
http_post_request = session.post(url, json=data)
print(http_post_request.text)
print(http_post_request.json())
print(http_post_request.status_code)
print(http_post_request.cookies)

session.close()