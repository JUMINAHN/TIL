import requests

URL = "http://google.com" #http 관련 정보를 받아온다
response = requests.get(url=URL) #요청을 받아온다
print(response.text)