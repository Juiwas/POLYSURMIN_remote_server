import json

import pandas as pd
from requests import post, get
from requests.auth import HTTPBasicAuth

api_address = "http://127.0.0.1:8000/"


# Проверка авторизации по логин-пароль-----------------------------------


df = pd.DataFrame({"velocity": [3, 14], "direction": [150, 14]})
data = {"data": df.to_dict('index')}

api_server = api_address + 'swan/results/'

response = post(api_server, json = json.dumps(data ) )
			
print('Логин-пароль:' ,response.status_code)
#print(response)
#if response:
#	print(response.json())

# Получаем токен-----------------------------------

#data = {"username": "admin", "password": "1234"}
data = {"username": "swan_user", "password": "12345670"}
api_server = api_address + "swan/api/token/" 
response = post(api_server, data=data)


print('Получение токена' ,response)
print('Получение токена' ,response.status_code)
user_token = response.json()


if response:
    print(response.json())
    user_token = response.json()


df = pd.DataFrame({"velocity": [3, 14], "direction": [150, 14]})
data = {"data": df.to_dict('index')}
headers = {'Authorization': 'Bearer {0}'.format(user_token['access'])}
api_server = api_address + "swan/api/token/results/"
response = get(api_server, headers=headers)

print('Запрос гет' , response.status_code)

if response:
    print(response.json())





			


"""
# Работаем по токену-----------------------------------

df = pd.DataFrame({"velocity": [3, 14], "direction": [150, 14]})
data = {"data": df.to_dict('index')}
headers = {'Authorization': 'Bearer {0}'.format(user_token['access'])}
api_server = api_address + "swan/api/token/results/"
response = post(api_server, headers=headers, json=json.dumps(data))

print('Отправка на счет' ,response.status_code)

if response:
    print(response.json())
"""

"""
# Просто проверка токена, если понадобиться -----------------------------------
api_server = api_address + "swan/api/token/verify/"
response = post(api_server, data={'token':user_token['access']})
print('Просто проверка токена' ,response.status_code)
if response:
    print(response.json())
"""
# Обновляем токен -----------------------------------

api_server = api_address + "swan/api/token/refresh/"
response = post(api_server, data={'refresh': user_token['refresh']})

print('Обновление токена' ,response.status_code)

if response:
    print(response.json())
   







