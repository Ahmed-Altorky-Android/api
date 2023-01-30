import json
from django.http import JsonResponse
from products.models import Product
# لتسهيل عرض محتويات المودل
from django.forms.models import model_to_dict
# Create your views here.

def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
	#يتم تحديد المتغير الذي يحتوي علي الداله ويتم اختيار القيم 
        data=model_to_dict(model_data, fields=['id','title'])
    return JsonResponse(data)
