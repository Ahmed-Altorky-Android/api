import requests

endpoint = "http://127.0.0.1:8000/api/products/1/"

# رساله تعرض عند اختيار البوست
get_responce = requests.get(endpoint)
# hello ahmed
print(get_responce.json())
