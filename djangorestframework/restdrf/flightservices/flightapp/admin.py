from django.contrib import admin
from .models import *
class levelsr(admin.ModelAdmin):
    list_display=['id','flightnumber','operatingairlines','departurecity' ]
admin.site.register(Flight,levelsr)

class levels(admin.ModelAdmin):
    list_display=['id','flight','passengar', ]
admin.site.register(Reservation,levels)
