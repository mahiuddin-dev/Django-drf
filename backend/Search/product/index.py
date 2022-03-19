# index.py

from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Product

@register(Product)
class YourModelIndex(AlgoliaIndex):
    should_index = 'is_public'
    fields = [
        'title',
        'description',
        'price',
        'public',
        'user',
    ]
    tags = 'get_tags_list'
