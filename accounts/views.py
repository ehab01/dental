from django.shortcuts import render
from rest_framework.generics import GenericAPIView, UpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, serializers, status
from django.db.utils import IntegrityError
from .serializers import *
from core.model.base_response import BaseResponse
from django.contrib import auth



class SignupView(GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = SignupSerializer

    def post(self, request, format=None):
        response = BaseResponse()
        try:
            #check on user handle is empty or not
            if request.data.get('contact_number') is None or request.data.get('contact_number') == '':
                json_response = response.create_failure_response(
                    'Missing contact number')
                return Response(json_response, status=status.HTTP_200_OK)

            #check on user email is empty or not
            if request.data.get('first_name') is None or request.data.get('email') == '':
                json_response = response.create_failure_response(
                    'Missing first name')
                return Response(json_response, status=status.HTTP_200_OK)       

            signupSerializer = SignupSerializer(data=request.data)

            #validating sign up serializer data
            if not signupSerializer.is_valid():
                json_response = response.create_failure_response(
                    signupSerializer.errors)
                return Response(json_response, status=status.HTTP_200_OK)

            #validate password length
            if len(request.data['password']) < 8:
                json_response = response.create_failure_response(
                    'The password is too short. It must contain at least 8 characters.')
                return Response(json_response, status=status.HTTP_200_OK)

            #all data is valid , set user password and return success
            user = signupSerializer.save()
            user.set_password(user.password)
            user.save()
            serializedUsers = SignupSerializer(
                user, context={'request': request})
            json_response = response.create_success_response(
                serializedUsers.data)
            return Response(json_response)
            
        #exception handling   
        except IntegrityError as e:
            json_response = response.create_failure_response(
                "This user handle is already exists")
            return Response(json_response, status=status.HTTP_200_OK)
        except Exception as e:
            json_response = response.create_failure_response(str(e))
            return Response(json_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
