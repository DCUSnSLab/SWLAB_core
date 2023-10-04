import requests

url = 'http://localhost:8000/api/login'
data = {'username':'root',
        'password':'rootroot'}

session = requests.Session()

http_post_request = session.post(url, json=data)
print(http_post_request.text)
print(http_post_request.cookies)

print('insert Lecture')
url = 'http://localhost:8000/api/admin/lectureapi'
data = {'title':'test',
        'description':'testtest',
        'status':True,
        'year':2023,
        'semester':1,
        'lectype':1,
        'subtype':'subject'
        }
http_post_request = session.post(url, json=data)
print(http_post_request.text)
print(http_post_request.json())
print(http_post_request.status_code)
print(http_post_request.cookies)

session.close()