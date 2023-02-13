import requests

headers = {'Authorization': 'Token 1fd234eec510739fd54162c202e1326f00faa670'}
# use this page in product/views.py
endpoint = "http://127.0.0.1:8000/api/products/"
data = {
   'title' : 'all in one',
   'price' : 22.99
}
# لعرض محتويات الرابط
get_responce = requests.post(endpoint, json=data, headers=headers)

print(get_responce.json())
