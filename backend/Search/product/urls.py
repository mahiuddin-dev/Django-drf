from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('', views.ProductListCreateAPIView.as_view(), name='product_create'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product_view'),
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view(), name='product_update_view'),
    path('<int:pk>/delete/', views.ProductDeleteAPIView.as_view(), name='product_delete_view'),
]
