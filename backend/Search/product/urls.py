from urllib.parse import urlparse
from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.ProductCreateAPIView.as_view(), name='product_create'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product_view'),
]
