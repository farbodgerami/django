from django.urls import path

from base.views import productviews as views

urlpatterns = [
    path("create/", views.createproduct, name="productcreate"),
    path("", views.getproducts, name="products"),
    path("upload/", views.uploadimage, name="uploadimage"),
    path("top/", views.gettopproducts, name="topproducts"),
    path("update/<str:pk>/", views.updateproduct, name="productupdate"),
    path("<str:pk>/", views.getproduct, name="product"),
    path("<str:pk>/reviews/", views.createproductreview, name="createreview"),
    path("delete/<str:pk>/", views.deleteproduct, name="productdelete"),
]
