from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import UserActivity
from .serializers import UserActivitySerializer
from core.model.base_response import BaseResponse
from django.core.exceptions import ValidationError

class UserActivityView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserActivitySerializer

    def get(self, request, format=None):
        response = BaseResponse()
        try:
            activities = UserActivity.objects.filter(user=request.user)
            serialized_activities = UserActivitySerializer(activities, many=True)
            json_response = response.create_success_response(serialized_activities.data)
            return Response(json_response, status=status.HTTP_200_OK)
        except Exception as e:
            json_response = response.create_failure_response(str(e))
            return Response(json_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, format=None):
        response = BaseResponse()
        serializer = UserActivitySerializer(request.user ,data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                json_response = response.create_success_response(serializer.data)
                return Response(json_response, status=status.HTTP_201_CREATED)
            else:
                json_response = response.create_failure_response(serializer.errors)
                return Response(json_response, status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as e:
            json_response = response.create_failure_response(str(e))
            return Response(json_response, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            json_response = response.create_failure_response(str(e))
            return Response(json_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
