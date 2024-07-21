from django.db import models
from django.core.exceptions import ValidationError
from accounts.models import User


class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f'{self.title} on {self.date} from {self.start_time} to {self.end_time}'

    def clean(self):
        if self.start_time >= self.end_time:
            raise ValidationError("End time must be after start time")

        overlapping_appointments = Appointment.objects.filter(
            user=self.user,
            date=self.date,
            start_time__lt=self.end_time,
            end_time__gt=self.start_time
        ).exclude(pk=self.pk)

        if overlapping_appointments.exists():
            raise ValidationError("This appointment conflicts with another appointment.")

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Appointments"
