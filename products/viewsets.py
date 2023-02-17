from rest_framework import mixins,viewsets

from .models import Product
from .serializers import ProductSerializers

class ProductViewSet(viewsets.ModelViewSet):
    '''
    Get -> list
    Get -> ditail from pk in urls
    Post -> create New product
    Post -> update product
    delete -> destroy product
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'pk' #defualt


class ProductGenericViewSet(
        mixins.ListModelMixin,
        mixins.RetrieveModelMixin,
        viewsets.GenericViewSet,):
    '''
    Get -> list
    Get -> ditail from pk in urls
    '''
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
