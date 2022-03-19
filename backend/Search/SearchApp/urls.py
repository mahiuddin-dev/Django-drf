from django.urls import path
from . import views

app_name = 'SearchApp'


urlpatterns = [
    path('',views.SearchListView.as_view(), name='search'),
]
