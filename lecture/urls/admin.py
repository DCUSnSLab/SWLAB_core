from ..views.admin import LectureAPI
from django.urls import re_path

urlpatterns = [
    re_path(r"^lectureapi/?$", LectureAPI.as_view(), name="lecture_api"),
]