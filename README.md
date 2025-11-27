### url-name
in root:
```py
from django.urls import include, path

urlpatterns = (
    [
       ...
        path("companies/", include("companies.urls", namespace="companies")),
    ]
)
```
in app:
```py
app_name = "companies"
urlpatterns = [
path("",views.CompanyViewSet.as_view({"get": "list", "post": "create"}),name="index"),
...
]
```
changed app_name and name, in postman no problem happned:
```
http://127.0.0.1:8000/companies/sendemail/
```

but in pytest, reverse function uses name and namespace:
```py
companies_url = reverse("namespace:name")
companies_url = reverse("companies:index")
```
### celery
in settings.py
```py

INSTALLED_APPS = [
...
    'django_celery_beat',
]
CELERY_BROKER_URL= 'redis://redis:6379/1'
CELERY_BEAT_SCHEDULER = 'django_celery_beat.schedulers:DatabaseScheduler'
```

in project root create a file name it celery.py and copy this:
```py
import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '<ROOT_APP_NAME>.settings')

app = Celery('<ROOT_APP_NAME>')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


```

in __init__.py of the root project:
```py
# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

__all__ = ('celery_app',)
```

now in related apps create a file name tasks.py and define a task:
```py
from celery import shared_task
from django.http import HttpResponse
import time

@shared_task
def sendEmail():
    for i in range(2):
      time.sleep(1)
      print(i)
```
now in views.py use that task:
```py
from django.shortcuts import render
from django.http import HttpResponse
import time
from .tasks import sendEmail
# Create your views here.
def send_email(request):
    j=sendEmail.delay()
    return HttpResponse(f"<h1>Done Sending</h1>")
```

### endpoints
### Cache
in settings.py
```py
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
} 
```
### filter
views.py
```py
class PostViewSet(viewsets.ModelViewSet):
    queryset=Post.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'author','status',]
    search_fields = ["title", "content"]
    ordering_fields = ["published_date"]
    pagination_class = MyPaginationClass

 
    filterset_fields = {
        "category": ["exact", "in"],#category_in=&category=
        "author": ["exact"],
        "status": ["exact"],
    }
```
urls.py
```py
urlpatterns = [
    path('post/',views.PostViewSet.as_view({'get':'list','post':'create' }),name="post_list"),
      path('post/<int:pk>/',views.PostViewSet.as_view({ 'get': 'retrieve','upda te':'put','patch':'partial_update','delete':'destroy'}),name="post_detail"),...
]
```
### pagination
### swagger
### pytest
### change user model

### all types of models from all projects
#### limited choices
to have limited choices use TextChoices:
```py
from django.db.models import URLField
class Company(models.Model):
    class CompanyStatus(models.TextChoices):
        LAYOFFS = "Layoffs"
        HIRING_FREEZE = "Hiring Freeze"
        HIRING = "Hiring"

    name = models.CharField(max_length=30, unique=True)
    status = models.CharField(
        choices=CompanyStatus.choices, default=CompanyStatus.HIRING
    )
    last_update = models.DateTimeField(default=now, editable=True)
    application_link = URLField(blank=True, max_length=100)

    def __str__(self):
        return self.name

```
### all kinds of serializers from all projects

#### model serializer:
views.py
```py
class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all().order_by("-last_update")
    pagination_class = PageNumberPagination
```
seralizers.py 
```py
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"
```

urls.py
```py
app_name = "companies"
urlpatterns = [
path("",views.CompanyViewSet.as_view({"get": "list", "post": "create"}),name="index"),
path(="<int:pk>/",views.CompanyViewSet.as_view({"get": "retrieve","put": "update","patch": "partial_update","delete": "destroy",}),name="detail",),
...
]
```