from django.urls import path, include
from .views import Hellowapiview, userloginapiview
from profilesapi import views
from rest_framework import routers

router=routers.DefaultRouter() 
router.register('ooshakhlar',views.Helloviewset,basename='ooshakhlar')
# profilemodelviewset:
router.register('profile',views.UserProfileviewset)
router.register('feed',views.userprofilefeedviewset)
urlpatterns = [
  path('h1/',views.Hellowapiview.as_view()),
  path('h2/', Hellowapiview.as_view()),
  path('login/', userloginapiview.as_view()),
  path('',include(router.urls)),
 
  
]


 