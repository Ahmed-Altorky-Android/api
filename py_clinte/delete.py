import requests

product_id = input("What Is ID Products? \n")

try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} Is Not Found')

if product_id:
    # use this page in product/views.py
    endpoint = f"http://127.0.0.1:8000/api/products/{product_id}/delete/"

    # لعرض محتويات الرابط
    get_responce = requests.delete(endpoint)

    print(get_responce.status_code, get_responce.status_code==204)
