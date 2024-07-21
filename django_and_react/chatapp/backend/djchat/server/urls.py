from django.urls import path
from .views import *
app_name='barrens'
urlpatterns = [
 
    path("select/", ServerListViewSet.as_view({'get': 'list'}) , name="levels"),
     path("category/", CategoryListViewSet.as_view({'get': 'list'}) , name="category"),
  
]


 