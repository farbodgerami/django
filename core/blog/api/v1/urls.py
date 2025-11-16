from django.urls import path
from . import views
from django.urls.conf import include
from rest_framework.routers import DefaultRouter, SimpleRouter

router = DefaultRouter()
app_name = "api-v1"

# router.register( prefix='post',viewset=views.PostViewSet,basename='post')
# router.register( prefix='category',viewset=views.CategoryViewSet,basename='category')
# urlpatterns =router.urls
urlpatterns = [
    # functionbase:
    # path("post/", views.PostList , name="post-list"),
        # path("post/<int:id>/", views.PostDetail, name="post-detail"),
    # path("post/", views.PostList.as_view(), name="post-list"),
    # path("post/<int:id>/", views.PostDetail.as_view(), name="post-detail"),
    path('post/',views.PostViewSet.as_view({'get':'list','post':'create' }),name="post_list"),
      path('post/<int:pk>/',views.PostViewSet.as_view({ 'get': 'retrieve','upda te':'put','patch':'partial_update','delete':'destroy'}),name="post_detail"),
]
