 
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from profilesapi import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('profilesapi.urls')),
    path('apii/',views.Hellowapiview.as_view() )
]

 