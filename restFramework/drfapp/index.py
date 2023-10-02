from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register


from .models import Product, Account

@register(Product)
class productindex(AlgoliaIndex):
    #  should_index =
     fields = [
                
                'user',
                'pk',
                'name',
                'category',
                'price',
                'discount',
                'discount_price',
                ]


@register(Account)
class Accountindex(AlgoliaIndex):
     fields =[
            'user',
            'account_name',
            'age',
            'gender',
            'created'
        ]
     
# algoliasearch.register(Account)