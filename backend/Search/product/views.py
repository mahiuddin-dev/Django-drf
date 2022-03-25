from rest_framework import generics,mixins
from .models import Product
from .serializers import ProductSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.mixins import EditPermissionMixin,UserQuerySetMixin
from django.shortcuts import get_object_or_404

class ProductListCreateAPIView(UserQuerySetMixin,EditPermissionMixin,generics.ListCreateAPIView): 
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(owner=self.request.user)
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description') or None
        if description is None:
            description  = title
        serializer.save(user=self.request.user,description=description)
    

    # def get_queryset(self, *args, **kwargs):
    #     query = super().get_queryset(*args, **kwargs)
    #     user = self.request.user
    #     if not user.is_authenticated:
    #         return query.none()

    #     return query.filter(user=user)

class ProductDetailView(UserQuerySetMixin,EditPermissionMixin,generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'id'

class ProductUpdateAPIView(UserQuerySetMixin,EditPermissionMixin,generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
        

class ProductDeleteAPIView(UserQuerySetMixin,EditPermissionMixin,generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        # instance 
        super().perform_destroy(instance)


# Product mixins
class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView):

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)
    
    def post(self,request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        description = serializer.validated_data.get('description') or None
        if description is None:
            description  = title
        serializer.save(description=description)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

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

