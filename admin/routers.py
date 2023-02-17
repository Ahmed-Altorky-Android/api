from rest_framework.routers import DefaultRouter

from products.viewsets import ProductGenericViewSet
'''
    Get -> list
    Get -> ditail from pk in urls
    Post -> create New product
    Post -> update product
    delete -> destroy product
'''
router = DefaultRouter()
router.register('products', ProductGenericViewSet, basename='products')
urlpatterns = router.urls