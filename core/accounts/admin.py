from django.contrib import admin

from .models import *
 
# class usershow(admin.ModelAdmin):
#         list_display=['id','email','is_staff','is_active' ]
#         list_filter=['email','is_staff','is_active' ]
#         search_fields=['email']


 
# admin.site.register(User,usershow)

from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):
    model=User
    list_display=['id','email','is_staff','is_active' ]
    list_filter=['email','is_staff','is_active' ]
    search_fields=['email']
    ordering=['email']
    fieldsets=(('Authentication',{"fields":('email','password'),}),
               ('Permissions',{"fields":('is_staff','is_active','is_superuser'),}),
               ('group_permissions',{"fields":('groups','user_permissions')},),
               ('important_date',{"fields":('last_login',)}),
               )
    add_fieldsets=(
        (None,{
            # 'classes':('wide'),
            'fields':('email','password1','password2','is_staff','is_active','is_superuser'),
        },),
    )
admin.site.register(User,CustomUserAdmin)
