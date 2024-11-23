from django.contrib import admin
from django.contrib.auth.models import User as x
from django.contrib.auth.models import Group
from .models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

class UserAdmin(BaseUserAdmin):
    fieldsets = (
        (None, {'fields': ('contact_number', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'user_email', 'age','player_id','contact_emergency')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('contact_number', 'password1', 'password2'),
        }),
    )
    list_display = ('contact_number', 'first_name', 'last_name', 'is_staff')
    search_fields = ('contact_number', 'first_name', 'last_name')
    ordering = ('first_name','last_name')

admin.site.site_header = "DentaLab administration"
admin.site.site_title = "App administration"
# admin.site.index_title = "Welcome to Your Custom Admin"
admin.site.register(User, UserAdmin)

# admin.site.register(User)
admin.site.register(Configuration)

# Register your models here.
