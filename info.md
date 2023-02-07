in views.py

'new massage4'
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
# استدعاء القيمه من الفيو
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
------------------------------------

# تحويل الانشاء الي ليسته عرض المنتجات 
-- in product/views.py
# لعرض الليست اذا كان جيت ويتم انشاء منتج اذا استخدمنا البوست
class ProductListCreateAPIView(generics.ListCreateAPIView):
   queryset = Product.objects.all()
   serializer_class = ProductSerializers

   def perform_create(self, serializer):
      #print(serializer.validated_data)
      title = serializer.validated_data.get('title')
      content = serializer.validated_data.get('content')
      if content is None:
         content = title
      serializer.save(content=content)

product_list_create_view = ProductListCreateAPIView.as_view()


-- mkdir py_clint/list.py

import requests
# use this page in product/views.py
endpoint = "http://127.0.0.1:8000/api/products/"

# لعرض محتويات الرابط
# هنا استخدمنا الجين فسوف تاتي باكل المنتجات
get_responce = requests.get(endpoint) »» لعرض المنتجات

print(get_responce.json())

-- in views.py 
	from rest_framework.response import Response
	from rest_framework.decorators import api_view
	from django.shortcuts import get_object_or_404

	@api_view(['GET','POST']) >> use api get and post in function
	def product_alt_view(request, pk=None, *args, **kwargs):
	method = request.method >> variable
	if method == "GET":
		if pk is not None: >> لو الاي دي موجود
			# detai view
			obj = get_object_or_404(Product, pk=pk) >> جلب المنتج من المودل والاي دي يساوي الايدي
			data = ProductSerializers(obj, many=False).data >>
			ملف الابياي نستخدم فيه المتغير اوبج جعل لا يوجد اكثر من منتج وبعد ذالك جلب البيانات
			return Response(data)
			#url > api/products/pk/ >> وهذا يجب وضع رقم المنتج فيه
		# list view
		# show all list view
		queryset = Product.objects.all()
		data = ProductSerializers(queryset, many=True).data >> العديد يوجد 
		return Response(data)
	if method == "POST":
		#create a product >> انشاء منتج لو بوست
		serializer = ProductSerializers(data=request.data)
		if serializer.is_valid():
			title = serializer.validated_data.get('title')
			content = serializer.validated_data.get('content') >> هذه محتويات المنتج المنشأ
			if content is None:
				content = title
			serializer.save(content=content)
			return Response(serializer.data)
-- in urls 
	from django.urls import path
	from . import views

	urlpatterns = [
		path('', views.product_alt_view),
		#path('', product_create_view),
		path('<int:pk>/', views.product_alt_view),
	]

-- error > 'No time zone found with key UTC'
-- resolve > pip install tzdata


-- in views.py 

class ProductUpdateAPIView(generics.UpdateAPIView): - للتعديل علي المنتجclass ProductUpdateAPIView(generics.UpdateAPIView):
   # queryset and serializer_class is important value
   queryset = Product.objects.all()  - جلب جميع المنتجات
   serializer_class = ProductSerializers  - جلب الدالة 
   lookup_field = 'pk' - التحديد عن طريق البي كي 

   def perform_update(self, serializer): - داله بها نفسي والدالة
      instance = serializer.save() - حفظ التعديل
      if not instance.content: - لو مش موجود 
         instance.content = instance.title - بدله بده

product_update_view = ProductUpdateAPIView.as_view() - متغير يستخدم في الرابط

-- in urls.py 

path('<int:pk>/update/', views.product_update_view), 
 - رابط به بي كي المنتج وعمل تعظيل عليه

-- in py_clint create file update.py

import requests
# use this page in product/views.py
endpoint = "http://127.0.0.1:8000/api/products/1/update/" - الرابط

data={
     'title': 'is update product', - المعلومات اللتي سوف يتم التعديل عليها 
     'price': 20.01
}

# لعرض محتويات الرابط
get_responce = requests.put(endpoint, json=data) نستخدم بت بدل جيت 
-- put - تستخدم اذا كان المنتج موجود وتريد استبدال معلومات فيه 
بمعلومات اخري مكانها 
print(get_responce.json())

--------------------------------------

-- in product/viewspy

class ProductDestroyAPIView(generics.DestroyAPIView): - دالة حذف المنتجات 
   # queryset and serializer_class is important value
   queryset = Product.objects.all()
   serializer_class = ProductSerializers
   lookup_field = 'pk'

   def perform_destroy(self, instance):
      super().perform_destroy(instance) 

product_destroy_view = ProductDestroyAPIView.as_view()


-- in urls.py

path('<int:pk>/delete/', views.product_destroy_view), - الرابط يأخذ اي دي المنتج مع الحذف


-- in py_clint mkfile delete.py

import requests

product_id = input("What Is ID Products? \n")

try:
    product_id = int(product_id) - من نو الارقام
except:
    product_id = None - جعله لا يساوي شئ
    print(f'{product_id} Is Not Found') - اذا لم يكن غير موجود

if product_id: لو كتب رقم 
    # use this page in product/views.py
    endpoint = f"http://127.0.0.1:8000/api/products/{product_id}/delete/"
    - نستخدم الرقم ونحذف المنتج

    # لعرض محتويات الرابط
    get_responce = requests.delete(endpoint) - حذف المنتج 

    print(get_responce.status_code, get_responce.status_code==204) 
    - لعرض هل الكود نجح ام لا مع رقم الصفحه 
