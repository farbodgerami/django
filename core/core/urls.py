from django.contrib import admin


from django.urls.conf import include
from django.conf.urls.static import static

from django.urls import path, re_path
from django.conf import settings
from django.views.generic import TemplateView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authtoken import views
from rest_framework.documentation import include_docs_urls

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    # permission_classes=[permissions.IsAdminUser],
)


urlpatterns = (
    [
        path("admin/", admin.site.urls),
        # loginlogout in browser
    path('api-auth/', include('rest_framework.urls')),
        path("blog/", include("blog.urls"), name="blog"),
        path("accounts/", include("accounts.urls"), name="accounts"),
        path("api-docs/", include_docs_urls(title="api-sample")),
        path("abc.json", schema_view.without_ui(cache_timeout=0), name="schema-json"),
        path('swagger/output.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)

# pip inw5qll coreapi pyyaml
# docker-compose exec backend sh -c "pip install coreapi pyyaml"
