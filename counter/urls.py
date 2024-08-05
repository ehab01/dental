from django.urls import path
from .views import UserActivityView
app_name = "user_activity_api"
urlpatterns = [
    path('user-activity/', UserActivityView.as_view(), name='user-activity'),
]