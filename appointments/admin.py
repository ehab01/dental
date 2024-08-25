from django.contrib import admin
from django.core.exceptions import ValidationError
from django.contrib import messages
from .models import Appointment
from core.helpers import send_push_notification
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'date', 'start_time', 'end_time')

    def save_model(self, request, obj, form, change):
        try:
            obj.save()
            if obj.user.player_id:
                title = "New Appointment Scheduled"
                message = f"An appointment has been scheduled for {obj.date} from {obj.start_time} to {obj.end_time}."
                send_push_notification(obj.user.player_id, title, message)
        except ValidationError as e:
            messages.error(request, e.message)

admin.site.register(Appointment, AppointmentAdmin)
