from django.db import models
from django.conf import settings
from django.db.models import Q

import random
# Create your models here.

TAGS_MODEL_VALUE = ['education', 'entertainment', 'food', 'health', 'sport', 'travel']

User = settings.AUTH_USER_MODEL

class ProductQuerySet(models.QuerySet):
    def is_public(self):
        return self.filter(public=True)

    def search(self, query,user=None):
        lookup = Q(title__icontains=query) | Q(description__icontains=query)
        qs = self.is_public().filter(lookup)
        if user is not None:
            qs2 = self.filter(user=user).filter(lookup)
            qs = (qs | qs2).distinct()
        return qs

class ProductManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return ProductQuerySet(self.model, using=self._db)

    def search(self, query, user=None):
        return self.get_queryset().is_public().search(query,user=user)

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, default=1, null=True)
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000, default=99.99)
    public = models.BooleanField(default=True)
    
    objects = ProductManager()

    @property
    def sale_price(self):
        return "%.2f" % (float(self.price)*0.8)
    
    def get_discount(self):
        return '123'

    def __str__(self):
        return self.title

    def is_public(self) -> bool:
        return self.public
    
    def get_tags_list(self):
        return [random.choice(TAGS_MODEL_VALUE)]