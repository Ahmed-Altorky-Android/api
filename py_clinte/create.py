import requests
# use this page in product/views.py
endpoint = "http://127.0.0.1:8000/api/products/"
data = {
   'title' : 'this field is nice',
   'price' : 22.99
}
# لعرض محتويات الرابط
get_responce = requests.post(endpoint, json=data)

print(get_responce.json())