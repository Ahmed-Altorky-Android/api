in views.py

-- replace JsonResponse
from rest_framework.response import Response

-- add apiview important
from rest_framework.decorators import api_view

-- add before def function
@api_view(["GET"]) 

-- use serializers and product_models in data function
in views.py
data=ProductSerializers(instance).data

tap error >> chang tap
