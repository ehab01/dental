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

            # #check on user email is empty or not
            # if request.data.get('first_name') is None or request.data.get('first_name') == '':
            #     json_response = response.create_failure_response(
            #         'Missing first name')
            #     return Response(json_response, status=status.HTTP_200_OK)       

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
            serializedUsers = getMyProfileSerializer(
                user, context={'request': request})
            json_response = response.create_success_response(
                serializedUsers.data)
            return Response(json_response)
            
        #exception handling   
        except IntegrityError as e:
            json_response = response.create_failure_response(
                e)
            return Response(json_response, status=status.HTTP_200_OK)
        except Exception as e:
            json_response = response.create_failure_response(str(e))
            return Response(json_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class LoginView(GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        response = BaseResponse()
        try:
            loginSerializer = LoginSerializer(data=request.data)
            if not loginSerializer.is_valid():
                json_response = response.create_failure_response(
                    loginSerializer.errors)
                return Response(json_response, status=status.HTTP_200_OK)

            user = auth.authenticate(contact_number=loginSerializer.validated_data['contact_number'], password=loginSerializer.validated_data['password'])
            
            print(user)
            if user is None:
                json_response = response.create_failure_response(
                    "Wrong contact number or password")
                return Response(json_response)

            serializedUsers = getMyProfileSerializer(
                user, context={'request': request})
            json_response = response.create_success_response(
                serializedUsers.data)
            return Response(json_response)

        except Exception as e:
            json_response = response.create_failure_response(str(e))
            return Response(json_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


class LogoutView(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, format=None):
        base_response = BaseResponse()
        try:
            logged_user = request.user

            if logged_user.player_id:
                User.objects.filter(id=request.user.id).update(
                    player_id=None)

            logged_user.auth_token.delete()
            json_response = base_response.create_success_response(
                "Logged Out Successfully")
            return Response(json_response, status=status.HTTP_200_OK)
        except Exception as e:
            json_response = base_response.create_failure_response(str(e))
            return Response(json_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UpdatePlayerIdView(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UpdatePlayerIdSerializer

    def post(self, request, format=None):
        response = BaseResponse()
        try:
            user = request.user
            update_player_id_serializer = UpdatePlayerIdSerializer(
                user, data=request.data, partial=True)
            if not update_player_id_serializer.is_valid():
                json_response = response.create_failure_response(
                    update_player_id_serializer.errors)
                return Response(json_response, status=status.HTTP_200_OK)
            user_data = getMyProfileSerializer(
                update_player_id_serializer.save(), context={'request': request})
            json_response = response.create_success_response(
                user_data.data)
            return Response(json_response)
        except Exception as e:
            json_response = response.create_failure_response(str(e))
            return Response(json_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)          


class UserProfileView(GenericAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = UserProfileSerializer

    def get(self, request, format=None):
        response = BaseResponse()
        try:
            user = request.user
            user_serializer = UserProfileSerializer(user)
            json_response = response.create_success_response(user_serializer.data)
            return Response(json_response, status=status.HTTP_200_OK)
        except Exception as e:
            json_response = response.create_failure_response(str(e))
            return Response(json_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ConfigurationView(GenericAPIView):
    permission_classes = (permissions.AllowAny,)
    serializer_class = ConfigurationSerializer

    def get(self, request, format=None):
        response = BaseResponse()
        try:
            config = Configuration.objects.first()  # Assuming only one config entry exists
            if not config:
                json_response = response.create_failure_response('No configuration found')
                return Response(json_response, status=status.HTTP_404_NOT_FOUND)

            config_serializer = ConfigurationSerializer(config)
            json_response = response.create_success_response(config_serializer.data)
            return Response(json_response, status=status.HTTP_200_OK)
        except Exception as e:
            json_response = response.create_failure_response(str(e))
            return Response(json_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)