
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls', namespace='api')),
    path('api/product/', include('product.urls', namespace='product')),
    path('api/v2/', include('Search.routers')),
]
