from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(owner=self.request.user)
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description') or None
        if description is None:
            description  = title
        serializer.save(description=description)


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


# Create, Detail View
@api_view(['GET','POST'])
def product_alt_view(request,pk=None,*arg,**kwargs):
    method = request.method
    if method == 'GET':
        if pk is not None:
            obj = get_object_or_404(Product,pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)

        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset,many=True)
        return Response(serializer.data)
    else:
        # Create an iteam
        serializer = ProductSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            # serializer.save()
            title = serializer.validated_data.get('title')
            description = serializer.validated_data.get('description') or None
            
            if description is None:
                description  = title
            
            serializer.save(description=description)
            
            return Response(serializer.data)
        return Response({'Invalid':'Invalid data'}, status=400)

