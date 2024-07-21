from django.contrib import admin

from .models import *

class levelsr(admin.ModelAdmin):
    list_display=['id','username','email','paidnuntil' ]
admin.site.register(User,levelsr)