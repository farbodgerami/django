from django.urls import path
from avval import views

app_name = 'chat'

urlpatterns = [
    path('<int:seconds>/', views.index, name='index'),
    path('a/<int:seconds>/', views.indexx, name='index1'),
    path('az/<int:seconds>/', views.test, name='index2'),
    path('as/<int:seconds>/', views.testasync, name='index3'),
 
 
]
