from django.db import models
from django.conf import settings

# Create your models here.
User = settings.AUTH_USER_MODEL

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, default=1, null=True)
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10000, default=99.99)
    
    @property
    def sale_price(self):
        return "%.2f" % (float(self.price)*0.8)
    
    def get_discount(self):
        return '123'

    def __str__(self):
        return self.title