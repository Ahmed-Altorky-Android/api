import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import Product
from products.serializers import ProductSerializers
# لتسهيل عرض محتويات المودل
from django.forms.models import model_to_dict
# Create your views here.

#@api_view(["GET"])
@api_view(["POST"])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializers(data=request.data)
    if serializer.is_valid():
      print(serializer.data)
      data=serializer.data
      return Response(data)


"""
@api_view(["POST"])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        #يتم تحديد المتغير الذي يحتوي علي الداله ويتم اختيار القيم
        #data=model_to_dict(model_data, fields=['id','title'])
       data=ProductSerializers(instance).data
    return Response(data)
"""
