from rest_framework import serializers
from accounts.models import *
from rest_framework.authtoken.models import Token


class SignupSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=200, required=True)

    class Meta:
        model = User
        fields = ['contact_number','first_name','last_name','contact_emergency','age','user_email','password']
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
        fields = ['id','token','player_id','contact_number','first_name','last_name','contact_emergency','age','user_email']  
    
    def get_token(self, obj):
            token, created = Token.objects.get_or_create(user=obj)
            return token.key
 


class UpdatePlayerIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['player_id']

class UserProfileSerializer(serializers.ModelSerializer):
    survey_link = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'contact_number', 'contact_emergency', 'user_email', 'age', 'player_id','survey_link'] 
        
    def get_survey_link(self, obj):
        # Fetch the Configuration object
        configuration = Configuration.objects.first()
        # Return the survey_link if the configuration exists, else return None
        return configuration.survey_link if configuration else None        



class ConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Configuration
        fields = ['survey_link']