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

--in products/views.py
	from rest_framework import generics
	from .models import Product
	from .serializers import ProductSerializers
	# Create your views here.
	# لعرض المنتجات
	class ProductDetailAPIView(generics.RetrieveAPIView):
   		#الاسمتء هنا اساسيه
		queryset = Product.objects.all()
   		serializer_class = ProductSerializers
   		#يجب ان يكون الرابط به اي دي المنتج
		# lookup_field = 'pk'
	# متغير به قيمه سنستخدمها في الرابط
	product_detail_view = ProductDetailAPIView.as_view()

-- in product/urla.py

from django.urls import path
# استعاء القيمه من الفيو
from .views import product_detail_view 

urlpatterns = [
    # استخام اي دي المنتج 
    path('<int:pk>/', product_detail_view)
]
