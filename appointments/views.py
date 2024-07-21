from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Appointment
from .serializers import AppointmentSerializer
from core.model.base_response import BaseResponse
from django.core.exceptions import ValidationError

class UserAppointmentsView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = AppointmentSerializer

    def get(self, request, format=None):
        response = BaseResponse()
        try:
            appointments = Appointment.objects.filter(user=request.user)
            serialized_appointments = AppointmentSerializer(appointments, many=True)
            json_response = response.create_success_response(serialized_appointments.data)
            return Response(json_response, status=status.HTTP_200_OK)
        except Exception as e:
            json_response = response.create_failure_response(str(e))
            return Response(json_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request, format=None):
        response = BaseResponse()
        try:
            data = request.data
            appointment = Appointment(
                user=request.user,
                title=data['title'],
                description=data.get('description', ''),
                date=data['date'],
                start_time=data['start_time'],
                end_time=data['end_time']
            )
            appointment.clean()
            appointment.save()
            serialized_appointment = AppointmentSerializer(appointment)
            json_response = response.create_success_response(serialized_appointment.data)
            return Response(json_response, status=status.HTTP_201_CREATED)
        except ValidationError as e:
            json_response = response.create_failure_response(str(e))
            return Response(json_response, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            json_response = response.create_failure_response(str(e))
            return Response(json_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
