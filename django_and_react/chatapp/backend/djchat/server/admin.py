from django.contrib import admin

# Register your models here.
from .models import *
 

class channelShow(admin.ModelAdmin):
    list_display=('id','name','owner', 'topic','server')
admin.site.register(Channel,channelShow)


class serverShow(admin.ModelAdmin):
    list_display=('id','name','owner', 'category')
admin.site.register(Server,serverShow)


class categoryShow(admin.ModelAdmin):
    list_display=('id','name')
admin.site.register(Category,categoryShow)