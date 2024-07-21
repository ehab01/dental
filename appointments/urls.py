from django.urls import path
from .views import UserAppointmentsView
app_name = "appointments_api"
urlpatterns = [
    path('api/appointments/', UserAppointmentsView.as_view(), name='user-appointments'),
]