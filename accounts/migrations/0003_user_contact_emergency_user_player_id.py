# Generated by Django 5.0.6 on 2024-08-05 20:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_user_contact_emergency_remove_user_player_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='contact_emergency',
            field=models.CharField(max_length=11, null=True, validators=[django.core.validators.RegexValidator(message='Phone number must be exactly 11 digits.', regex='^\\d{11}$')]),
        ),
        migrations.AddField(
            model_name='user',
            name='player_id',
            field=models.TextField(blank=True, null=True),
        ),
    ]
