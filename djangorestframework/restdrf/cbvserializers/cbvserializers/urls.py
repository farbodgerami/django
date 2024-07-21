from django.contrib import admin
from django.urls import path,include
from cbvapp import views
from rest_framework.routers import DefaultRouter
from cbvapp.views import *

router=DefaultRouter()
# router.register('students',views.Studentviewset)
router.register('user',views.Userviewset)

# urlpatterns = [
#     # path('admin/', admin.site.urls),
#     path('',include(router.urls)),
#     path('admin/', admin.site.urls), 
# ]

urlpatterns = [
    path('students/',views.student_list.as_view()),
    path('students/<int:pk>',views.student_detail.as_view()),
    path('',include(router.urls)),
     path('auth/',Customobtainauthtoken.as_view()),
]
