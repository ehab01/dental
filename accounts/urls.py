from django.urls import re_path
from .views import SignupView

app_name = "accounts_api"

urlpatterns = [
    re_path(r'^signup$', SignupView.as_view(), name="sign_up"),
]
