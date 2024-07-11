from django.urls import re_path
from .views import SignupView , LoginView ,LogoutView

app_name = "accounts_api"

urlpatterns = [
    re_path(r'^signup$', SignupView.as_view(), name="sign_up"),
     re_path(r'^signin$', LoginView.as_view(), name="sign_in"),
       re_path(r'^signout$', LogoutView.as_view(), name="sign_out"),
]
