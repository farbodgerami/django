from django.contrib import admin
from .models import *

admin.site.register(Product)

admin.site.register(Review)
admin.site.register(Order)
admin.site.register(Orderitem)
admin.site.register(Shippingadress)