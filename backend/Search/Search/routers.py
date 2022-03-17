from rest_framework.routers import DefaultRouter

from product.viewsets import ProductViewsets

routers = DefaultRouter()
routers.register('products', ProductViewsets, basename='products')

urlpatterns = routers.urls