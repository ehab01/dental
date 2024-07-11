from django.db import models
from django.contrib.auth.models import AbstractUser , Group, Permission
from django.db import IntegrityError

class User(AbstractUser):

    first_name= models.CharField(max_length=10,unique=False,null=False)
    last_name = models.CharField(max_length=10,unique=False,null=False)
    contact_number = models.CharField(max_length=11,unique=True,null=False) 
    contact_emergency = models.CharField(max_length=11,unique=False,null=False)  
    player_id = models.TextField(null=True,blank=True)  
         
    USERNAME_FIELD = "contact_number"
    REQUIRED_FIELDS = ["username"]

    def save(self, *args, **kwargs):
        self.username = self.contact_number
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.contact_number)

    class Meta:
        verbose_name_plural = "Users"