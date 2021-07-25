import requests
import json


payload = {
    'user_phone':'+7 926 200 15 17',
    'user_email':"petya@go.ru",
    'subjects': 'text',
    'order_date':'2021-07-23'
}

headers = {'content-type': 'application/json'}

ret = requests.post('http://127.0.0.1:5000/get_form', data=json.dumps(payload), headers=headers)

print(ret.text)