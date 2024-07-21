from django.urls import path
from base.views import userviews as views

urlpatterns = [
    path("login", views.MyTokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("loginman", views.loginman, name="token_obtain_pair"),
    path("register/", views.registeruser, name="register"),
    path("profile/update", views.updateuserprofile, name="updateusersprofile"),
    path("", views.getuser, name="users"),
    path("delete/<str:id>", views.deleteuser, name="userdelete"),
    path("update/<str:id>/", views.updateuser, name="userupdate"),
    path("profile/", views.getuserprofile, name="usersprofile"),
    path("<str:id>", views.getuserbyid, name="user"),
]
