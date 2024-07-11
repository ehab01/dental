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



class LoginSerializer( serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['contact_number', 'password']
        extra_kwargs = {'contact_number': {'required': True, 'validators': []},
                        'password': {'required': True}}        
        



class getMyProfileSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['id','token','contact_number','contact_emergency', 'first_name','last_name']   
    
    def get_token(self, obj):
            token, created = Token.objects.get_or_create(user=obj)
            return token.key
 
 