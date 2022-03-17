from rest_framework import serializers
from .models import Product

def validate_title(value):
    qs = Product.objects.filter(title__iexact=value)

    if qs.exists():
        raise serializers.ValidationError(f" {value} This title has already been used")
    return value