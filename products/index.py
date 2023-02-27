from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register
from .models import Product



# example > admin.site.register(Product)
@register(Product)
class ProductIndex(AlgoliaIndex):
    #should_index = 'is_public'
    fields = [
        'title',
        'content',
        'price',
        'user',
        'public'
    ]
    settings = {
        'searchableAttributes': ['title', 'body'],
        'attributesForFaceting': ['user', 'public']
    }
    tags = 'get_tags_list'