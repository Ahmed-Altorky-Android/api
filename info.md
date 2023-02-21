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

-- in views.py 
	- from rest_framework import generics, mixins -- خليط لدمج اومر الاريست في دالة واحده
	class ProductMixinView(
		mixins.CreateModelMixin,          						   -- انشاء منتج
		mixins.ListModelMixin,                                     -- عرض جميع المنتجات
		mixins.RetrieveModelMixin,                                 -- لعرض تفاصيل المنتج
		generics.GenericAPIView                                    -- يستخدم مع المكسن لاضاغة اكثر من فئه
		):
		
		queryset = Product.objects.all()
		serializer_class = ProductSerializers
		lookup_field = 'pk'

		def get(self, request, *args, **kwargs): #Http ->> get     -- استخدام طريقة جيت
			pk = kwargs.get("pk")                                  -- جلب الرقم
			if pk is not None:                                     -- لو الرقم موجود
				return self.retrieve(request, *args, **kwargs)     -- لعرض تفاصيل المنتج الواحد
			return self.list(request, *args, **kwargs)             -- لعرض قائمة المنتجات
		def post(self, request, *args, **kwargs): #Http ->> post   -- استخدام طريقة بوست
			return self.create(request, *args, **kwargs)           -- انشاء منتج
		def perform_create(self, serializer):                      -- يمكن استخدام البرفورم الخاصة بالاانشاء
			#print(serializer.validated_data)
			title = serializer.validated_data.get('title')
			content = serializer.validated_data.get('content')
			if content is None:
				content = title
			serializer.save(content=content)
	product_mixin_view = ProductMixinView.as_view()

in urls.py
	path('', views.product_mixin_view),                            -- لعرض او انشاء منتج بالجيت للعرض او البوست للانشاء 
	path('<int:pk>/', views.product_mixin_view),                   -- لعرض تفاصيل منتج واحد من نوع الجيت
	

-- in views.py 
	from rest_framework import generics, mixins, permissions, authentication
	-- in class ProductListCreateAPIView
		permission_classes = [permissions.IsAuthenticated] #--> authenticated all -- لطلب تصريح في كل الصفحات
		authentication_classes = [authentication.SessionAuthentication] -- مصادقه في الخلفيه
		permission_classes = [permissions.IsAuthenticatedOrReadOnly] #--> التصريح في صفحات البوست فقط  
-- in urls.py
	path('', views.product_list_create_view),
	path('<int:pk>/', views.product_list_create_view),

---------------------------------------------

-- in settings.py installation app
	'rest_framework.authtoken',        -- تثبيت التوكن

-- in apiapp/urls.py
	from rest_framework.authtoken.views import obtain_auth_token
	path('auth/', obtain_auth_token),   -- رابط لجلب التوكن

-- in apiapp/authentication.py  -- ملف جديد
	from rest_framework.authentication import TokenAuthentication as BaseTokenAuth
	class TokenAuthentication(BaseTokenAuth):   -- استخدام التوكن
		keyword = 'Token'

-- in products/views.py 
	from apiapp.authentication import TokenAuthentication -- اضافة دالة التوكن من التطبيق
	authentication_classes = [
      authentication.SessionAuthentication,
      TokenAuthentication                                 -- استخدامها
   ]

-- in py_clinte/list.py
	import requests
	from getpass import getpass                           -- جلب الباسورد

	auth_endpoint = "http://localhost:8000/api/auth/"     -- رابط جلب التوكن
	username = input("What is your username?\n")          -- طلب اسم الحساب
	password = getpass("What is your password?\n")        -- طلب باسورد الحساب

	auth_response = requests.post(auth_endpoint, json={'username': username, 'password': password}) 
	-- استخدام الرابط مع جيسون وتعريف الاسم والباسورد بالمتغيرات
	print(auth_response.json())

	if auth_response.status_code == 200:                   -- لو البيانات صحيحه
		token = auth_response.json()['token']
		headers = {
			"Authorization": f"Token {token}"              -- كائن به محتوي
		}
		# use this page in product/views.py
		endpoint = "http://127.0.0.1:8000/api/products/"

		# لعرض محتويات الرابط
		get_responce = requests.get(endpoint, headers=headers)
		-- سوف يعرض الليست اذا تم تسجيل الدخول
		print(get_responce.json())

-- in py_clint/create.py
	headers = {'Authorization': 'Token 1fd234eec510739fd54162c202e1326f00faa670'}
	-- استخدام الهيدر لاضافة التوكن ويجب ان يكون التوكن تم انشائه
	get_responce = requests.post(endpoint, json=data, headers=headers) -- استخدام الهيدر


-- in settings.py end
	REST_FRAMEWORK = {
		"DEFAULT_AUTHENTICATION_CLASSES":[         -- انشاء قيمة افتراضيه للمصادقات
			'rest_framework.authentication.SessionAuthentication',
			'rest_framework.authentication.TokenAuthentication'
			-- هذه الاشياء تكون موجوده افتراضيا في الدوال
		],
		"DEFAULT_PERMISSION_CLASSES":[             -- انشاء قيمه افتراضية للاذونات
			'rest_framework.permissions.IsAuthenticatedOrReadOnly'
		]
	}

-- in apiapp create file permissions.py
	from rest_framework import permissions

	class IsEditPermissions(permissions.DjangoModelPermissions):
	 -- مكتبه خاصه بالمصادقه مع المودل وتختص بالعرض والتعديل والاضافه والحذف
		perms_map = { 
		'GET': ['%(app_label)s.view_%(model_name)s'], 
		'OPTIONS': [], 
		'HEAD': [], 
		'POST': ['%(app_label)s.add_%(model_name)s'], 
		'PUT': ['%(app_label)s.change_%(model_name)s'], 
		'PATCH': ['%(app_label)s.change_%(model_name)s'], 
		'DELETE': ['%(app_label)s.delete_%(model_name)s'], 
		} 
		-- لتعريف الادوات للمكتبه

-- in apiapp create file mixins.py
	from rest_framework import permissions
	from .permissions import IsEditPermissions  -- اضافة الدالة التي قمنا بانشائها

	class EditPermissionMixin():
		permission_classes = [permissions.IsAdminUser, IsEditPermissions]
		-- اضافة خليط من الدلة اللتي انشاناها مسبقا ودالة اخري وهي 
		-- IsAdminUser اذا كان المستخد قيد التسجيل وله الصلاحيات سوف يشتغل

-- in views.py
	from apiapp.mixins import EditPermissionMixin -- دالة الخليط اللتي انشاناها
test > 
	class ProductListCreateAPIView(
	EditPermissionMixin,                          -- يتم استخدامها بهذه الطريقه مع الدوال
	generics.ListCreateAPIView):
	-- وبهذا اذا تم منع الاذونات للجروب وتمت اضافه الجروب لليوزر ياخذ
	 صلاحيات الجروب تي وان كان ليس لديه صلاحيات

-- in product make file > viewsets.py
	from rest_framework import mixins,viewsets              -- لعرض جميع الصفحات واستخدامها مع اعادة التوجيه
	from .models import Product                      -- يتم اضافة دالة المودل
	from .serializers import ProductSerializers      -- Serializers يتم اضافة دلة 

	class ProductViewSet(viewsets.ModelViewSet):     -- لاستخدام مودل منشئه مسبقا
		queryset = Product.objects.all()
		serializer_class = ProductSerializers
		lookup_field = 'pk' #defualt                 -- يستخدم المفتاح الفريد لعرض منتج معين والتعديل عليه
	
	
	class ProductGenericViewSet(                     -- لتحديد المعروضات
			mixins.ListModelMixin,                   -- لعرض الليست
			mixins.RetrieveModelMixin,               -- لعرض التفاصيل
			viewsets.GenericViewSet,):
		'''
		Get -> list
		Get -> ditail from pk in urls                -- يستخدم الجيت فقط
		'''
		queryset = Product.objects.all()
		serializer_class = ProductSerializers
		-- يتم تغيير اسم الدلة في ملف اعادة التوجيه

-- in admin make file routers.py
	from rest_framework.routers import DefaultRouter -- لاعادة التوجيه

	from products.viewsets import ProductViewSet     -- ProductViewSet اضافة دالة 
	'''
		Get -> list                                  -- لعرض جميع المنتجات
		Get -> ditail from pk in urls                -- لاختيار منج معين بالمفتاح الفريد
		Post -> create New product                   -- لانشاء منج
		Post -> update product                       -- للتعديل علي منتج
		delete -> destroy product                    -- لحذف منتج
	'''
	router = DefaultRouter()                         -- استخدام اعادة التوجيه
	router.register('products', ProductViewSet, basename='products')
	--				 اسم العرض        ودالة العرض    ورابط العرض 
	urlpatterns = router.urls  

-- in admin/urls.py\
	-- https://localhost:port/api/v2/product-abc/
	path('api/v2/', include('admin.routers')),     -- يستخدم هذا الرابط للوصول الي الصفحه مع اضافة مسار الراوتر


-- in serializers.py
	from rest_framework.reverse import reverse         -- اضافة اعادة التوجيه
	class ProductSerializers(serializers.ModelSerializer):
		# edit_url = serializers.SerializerMethodField(read_only=True)  -- لاضافة فيلد معينه
		(1)-edit_url = serializers.HyperlinkedIdentityField(view_name='product-edit', lookup_field='pk')
		-- هنا اضفنا اسم ثم اضفنا اداة ربط برابط معين من خلال اسمه في ملف الروبط
		-- وهنا هذا لانشاء رابط وصول لصفحة التعديل علي المنتج
		url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')
		-- هنا اضفنا اسم ثم اضفنا اداة ربط برابط معين من خلال اسمه في ملف الروبط
		-- وهنا هذا لانشاء رابط وصول لصفحة عرض معلومات المنتج
		class Meta:
			model = Product
				fields = [
					'url', -- هذا الاسم الموجود في الاعلي لعرض المعلومات
					'edit_url',  -- وهذا للتعديل علي المنتج
					'id',
					'title',
					'content',
					'price',
					'get_descount',
				]
		def validate_title(self, value):   -- للتاكد من العنوان
			qs = Product.objects.filter(title__exact=value)  -- لفلترة العنوان
			if qs.exists():  -- لو العنوان موجود
				raise serializers.ValidationError(f"{value} is alredy product name")   
			return value	
		-------------------------------------
		# def get_edit_url(self, obj):
		#         request = self.context.get('request') #self.request
		#         if request is None:
		#              return None
		#         return reverse("product-edit", kwargs={'pk':obj.pk}, request=request)
		-- (1)هذا كله يستخدم بدل هذا 

-- in urls.py
	path('<int:pk>/update/', views.product_update_view, name='product-edit'), -- نضف الاسم
    path('<int:pk>/', views.product_detail_view, name='product-detail'),


-- in product/models.py
	from django.conf import settings   -- اضافة الاعدادات
	User = settings.AUTH_USER_MODEL    -- لجلب اليوزر من الاعدادات
	class Product(models.Model):
		user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
		-- لربط اليوزر بالمودل مع قيمه فارغه

-- in apiapp makefile serializers.py
	from rest_framework import serializers
	class UserPablicSerializers(serializers.Serializer):
		username = serializers.CharField(read_only=True) -- لتعريف اليوزر بانه حروف مع قرئه كل شئ
		id = serializers.IntegerField(read_only=True)    -- لتعريف رقم اليوزر

-- in product/serializers.py
from apiapp.serializers import UserPablicSerializers
class ProductSerializers(serializers.ModelSerializer):
    user = UserPablicSerializers(read_only=True)  -- لربط اليوزر الاصلي مع اليوزر اللذي انشءناه
	fields = [
        'user', -- لاظهار اسم اليوزر والايدي الخاص به