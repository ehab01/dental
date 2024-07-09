from rest_framework import serializers
from accounts.models import *
from rest_framework.authtoken.models import Token


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=200, required=True)

    class Meta:
        model = User
        fields = ['first_name','last_name','contact_number','contact_emergency','password']
        extra_kwargs = {'first_name': {'required': True},
                         'last_name': {'required': True},
                        'contact_number': {'required': True},
                        'contact_emergency': {'required': True},
                        }