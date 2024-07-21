from django.contrib import admin
from django.core.exceptions import ValidationError
from django.contrib import messages
from .models import Appointment

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date', 'start_time', 'end_time')

    def save_model(self, request, obj, form, change):
        try:
            obj.save()
        except ValidationError as e:
            messages.error(request, e.message)

admin.site.register(Appointment, AppointmentAdmin)
