from django.urls import re_path
from .views import SignupView , LoginView ,LogoutView , UpdatePlayerIdView,UserProfileView,ConfigurationView

app_name = "accounts_api"

urlpatterns = [
    re_path(r'^signup$', SignupView.as_view(), name="sign_up"),
     re_path(r'^signin$', LoginView.as_view(), name="sign_in"),
       re_path(r'^signout$', LogoutView.as_view(), name="sign_out"),
       re_path(r'^update-player-id$', UpdatePlayerIdView.as_view(), name="sign_out"),
        re_path('profile/', UserProfileView.as_view(), name='user-profile'),
        re_path('configurations/', ConfigurationView.as_view(), name='configuration'),
       
]
