from django.contrib import admin
from django.urls import path,include
from flightapp import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
router=DefaultRouter()
router.register('flights',views.Flightviewset)
router.register('passengars',views.Passengarviewset)
# router.register('reservation',views.Reservationviewset)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('khodamreserve/',views.Reservationlist.as_view()),
    path('khodamreserve/<int:pk>',views.Reservationdetail.as_view()),
    path('flightservices/findflights/',views.findflights),
    path('flightservices/savereservation/',views.savereservation),
     path('api-token-auth/', obtain_auth_token,name='apitokenauth')
]
