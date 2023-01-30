import json
from django.http import JsonResponse
from products.models import Product
# Create your views here.

def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data['id'] = model_data.id # show id
        data['title'] = model_data.title 
        data['content'] = model_data.content
        data['title'] = model_data.title
    return JsonResponse(data)