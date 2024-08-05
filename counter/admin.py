from django.contrib import admin
from .models import UserActivity

class UserActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'time_spent', 'timestamp')
    readonly_fields = ('timestamp',)

admin.site.register(UserActivity, UserActivityAdmin)