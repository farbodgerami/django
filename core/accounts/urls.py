from django.urls import path, include
from . import views

app_name = "accounts"
urlpatterns = [path("api/v1/", include("accounts.api.v1.urls"), name="api-v1"),
               path("api/v1/sendmail",views.send_email , name="api-v1"),
               ]
