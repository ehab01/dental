from django.urls import path
from .views import HomePageView
app_name = "home_api"
urlpatterns = [
    path('home/', HomePageView.as_view(), name='home_page'),
    # other URL patterns
]