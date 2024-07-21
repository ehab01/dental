from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ['id', 'title', 'description', 'date', 'start_time', 'end_time']

    def validate(self, data):
        if data['start_time'] >= data['end_time']:
            raise serializers.ValidationError("End time must be after start time")

        overlapping_appointments = Appointment.objects.filter(
            user=self.context['request'].user,
            date=data['date'],
            start_time__lt=data['end_time'],
            end_time__gt=data['start_time']
        ).exclude(pk=self.instance.pk if self.instance else None)

        if overlapping_appointments.exists():
            raise serializers.ValidationError("This appointment conflicts with another appointment.")

        return data
