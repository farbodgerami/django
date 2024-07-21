from django.db import router
from django.urls import path,include
from profilesapi import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()

urlpatterns = [
    path('hellow/',views.Helloapiview.as_view()), 
]
