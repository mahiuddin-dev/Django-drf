import json
from django.forms.models import model_to_dict
from django.shortcuts import render
# from django.http import JsonResponse
from product.models import Product

# Rest Framwork
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def api_home(request, *args, **kwargs):
    
    model_data = Product.objects.all().order_by('?').first()
    data = {}

    if model_data:
        data = model_to_dict(model_data,fields=['id','title','price'])
    
    return Response(data)

   