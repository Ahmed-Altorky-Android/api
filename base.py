import requests

endpoint = "http://127.0.0.1:8000/api/"

# رساله تعرض عند اختيار البوست
get_responce = requests.post(endpoint, json={'title': 'Hello World'})
# hello ahmed
print(get_responce.json())

# يجب التاكد من فتح السيرفر بااي بس 8000
# python manage.py runserver 8000
