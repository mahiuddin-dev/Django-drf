from django.contrib import admin

# Register your models here.
from . import models

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'sale_price', 'user')
    list_filter = ['user']
    search_fields = ('title', 'description',)
    
    class Meta:
        model = models.Product

admin.site.register(models.Product, ProductAdmin)