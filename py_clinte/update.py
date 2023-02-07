import requests
# use this page in product/views.py
endpoint = "http://127.0.0.1:8000/api/products/1/update/"

data={
     'title': 'is update product',
     'price': 20.01
}

# لعرض محتويات الرابط
get_responce = requests.put(endpoint, json=data)

print(get_responce.json())

