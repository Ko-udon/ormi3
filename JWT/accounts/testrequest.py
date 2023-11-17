import requests
# pip install requests

HOST = 'http://localhost:8000'
LOGIN_URL = HOST + '/account/login/'

LOGIN_INFO = {
  'email': 'ko@gmail.com',
  'password': 'ko12345@'
}

# 로그인을 위해 post요청을 보냅니다.
response = requests.post(LOGIN_URL, data=LOGIN_INFO)
print('==== status_code ====')
print(response.status_code)
print('==== text ====')
print(response.text)
print('==== json ====')
print(response.json())
print('==== access token ====')
print(response.json()['access_token'])

token = response.json()['access_token']
# 로그인한 사용자만 들어갈 수 있는 URL에 접속
# headers에 token을 넣어서 보냅니다.
header = {
    'Authorization': 'Bearer ' + token
}

data = {
  'title': '제목',
  'content': '내용',
  'author': 1
}

res = requests.get(HOST + '/account/test/', headers=header, data=data)
print(res.status_code)
print(res.text)