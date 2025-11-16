from django.urls import path
from . import views
from django.urls.conf import include

app_name = "blog"
urlpatterns = [
    path("about", views.indexView, name="funcviewTest"),

    path("test/", views.test, name="test"),
     path("post/", views.api_post_listview, name="api_post_listview"),
    path("api/v1/", include("blog.api.v1.urls"), name="api-v1"),
]
