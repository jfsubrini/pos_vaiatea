"""
bar URL Configuration
"""
from django.urls import path
from . import views


urlpatterns = [
    path("", views.bar, name="bar"),
]
