from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

app_name ='api'

urlpatterns = [
    path('auth/', obtain_auth_token),
    path('', views.api_home, name='api_home'),
]

