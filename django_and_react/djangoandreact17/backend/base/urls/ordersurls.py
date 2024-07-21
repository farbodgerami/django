from django.urls import path

 
 
from base.views import orderviews as views
urlpatterns=[
 path('',views.getRouts,name='usersprofile'),
 
]