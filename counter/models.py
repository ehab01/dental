from django.db import models
from django.core.exceptions import ValidationError
from accounts.models import User


class UserActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='FlossingLog')
    time_spent = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username} - {self.time_spent}s"
    class Meta:
        verbose_name_plural = "UserActivities"
