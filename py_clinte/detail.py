import requests
# use this page in product/views.py
endpoint = "http://127.0.0.1:8000/api/products/1/"

# لعرض محتويات الرابط
get_responce = requests.get(endpoint)

print(get_responce.json())
