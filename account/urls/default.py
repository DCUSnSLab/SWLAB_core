from ..views.default import Register, UserLoginAPI, UserTest
from django.urls import re_path

urlpatterns = [
    re_path(r"^register/?$", Register.as_view(), name="register_api"),
    re_path(r"^login/?$", UserLoginAPI.as_view(), name="login_api"),
    re_path(r"^logintest/?$", UserTest.as_view(), name="login_test_api"),
]
