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

	-- RetrieveAPIView   >> يستخدم للقرائه فقط لنقاط النهايه
	-- https://bit.ly/retreveapiview  >> معلومات حول العرض
	# لعرض المنتجات
	class ProductDetailAPIView(generics.RetrieveAPIView):
   		#الاسمتء هنا اساسيه
		queryset = Product.objects.all()
   		serializer_class = ProductSerializers
   		#يجب ان يكون الرابط به اي دي المنتج
		# lookup_field = 'pk'
	# متغير به قيمه سنستخدمها في الرابط
	product_detail_view = ProductDetailAPIView.as_view()

	# لانشاء المنتجات
	class ProductCreateAPIView(generics.CreateAPIView):
		queryset = Product.objects.all()
		serializer_class = ProductSerializers
		  def perform_create(self, serializer): >>  serializer لانشاء 
		  #print(serializer.validated_data) >> create.py لعرض الداتاالتي تم اضافتها في ملف 
		  title = serializer.validated_data.get('title') >> متغير به العنوان يساوي العنوان الموجود في الداتا
		  content = serializer.validated_data.get('content')>> متغير به المحتوي يساوي المحتوي الموجود في الداتا
		  if content is None: >> لو المحتوي فارغ
			content = title >> المحتوي يساوي العنوان
		  serializer.save(content=content) >> الحفظ مع المحتوي يساوي المحتوي اللي فوق
	# متغير به قيمه سنستخدمها في الرابط
	product_create_view = ProductCreateAPIView.as_view()	

-- in product/urla.py

from django.urls import path
# استعاء القيمه من الفيو
from .views import product_detail_view, product_create_view

urlpatterns = [
    # استخام اي دي المنتج 
    path('<int:pk>/', product_detail_view)و
	path('', product_create_view),
]

-- in py_clint mkfile create.py
	import requests
	# use this page in product/views.py
	endpoint = "http://127.0.0.1:8000/api/products/"
	# الداتا هيا التي يكون بها القيم الذي نضيف فيها 
	# في كل مره يتم تشغيل الملف يصنع منتج جديد بالمعلومات اللتي بداخل الداتا
	data = {
		'title' : 'this field is nice',
		'price' : 22.99
	}
	# لعرض محتويات الرابط
	get_responce = requests.post(endpoint, json=data)

	print(get_responce.json())
