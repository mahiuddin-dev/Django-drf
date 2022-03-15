from django.forms.models import model_to_dict
from product.models import Product
from product.serializers import ProductSerializer
# Rest Framwork
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)

    if serializer.is_valid(raise_exception=True):
        # serializer.save()
        data = serializer.data
        print(data)
        return Response(data)

    return Response({'Invalid':'Invalid data'}, status=400)



# @api_view(['GET'])
# def api_home(request, *args, **kwargs):
    
#     instance = Product.objects.all().order_by('?').first()
#     data = {}

#     if instance:
#         # data = model_to_dict(instance,fields=['id','title','price','sale_price'])
#         data = ProductSerializer(instance).data
    
#     return Response(data)

   