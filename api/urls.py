from django.urls import path
from .views import Grate

urlpatterns = [
    path('goldrate/',Grate.as_view()),
]