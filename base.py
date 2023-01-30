import requests

endpoint = "http://127.0.0.1:8000/api/"

get_responce = requests.get(endpoint, json={'product_id': 123})
# hello ahmed
print(get_responce.json())

# يجب التاكد من فتح السيرفر بااي بس 8000
# python manage.py runserver 8000
