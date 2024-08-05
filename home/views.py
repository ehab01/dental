from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from counter.models import UserActivity
from appointments.models import Appointment
from learning.models import Post
from counter.serializers import UserActivitySerializer
from appointments.serializers import AppointmentSerializer
from learning.serializers import PostSerializer
from core.model.base_response import BaseResponse
from django.utils import timezone
from datetime import datetime, timedelta

class HomePageView(GenericAPIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        response = BaseResponse()
        today = timezone.localdate()
        start_of_day = datetime.combine(today, datetime.min.time())
        end_of_day = start_of_day + timedelta(days=1)

        try:
            # Today's user activities
            activities = UserActivity.objects.filter(
                user=request.user,
                timestamp__gte=start_of_day,
                timestamp__lt=end_of_day
            )
            serialized_activities = UserActivitySerializer(activities, many=True)

            # Today's appointments
            appointments = Appointment.objects.filter(
                user=request.user,
                date=today
            )
            serialized_appointments = AppointmentSerializer(appointments, many=True)

            # Last 5 learning posts
            posts = Post.objects.all().order_by('-created_at')[:5]
            serialized_posts = PostSerializer(posts, many=True)

            # Combine all data
            data = {
                'today_activities': serialized_activities.data,
                'today_appointments': serialized_appointments.data,
                'recent_posts': serialized_posts.data
            }

            json_response = response.create_success_response(data)
            return Response(json_response, status=status.HTTP_200_OK)
        
        except Exception as e:
            json_response = response.create_failure_response(str(e))
            return Response(json_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
