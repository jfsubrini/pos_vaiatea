# -*- coding: utf-8 -*-
"""
schedule URL Configuration
"""
from django.urls import path
from . import views


urlpatterns = [
    path("guest/creation/", views.guest_creation, name="guest-creation"),
    path("guest/update/", views.guest_update, name="guest-update"),
    path("guest/list/", views.guest_list, name="guest-list"),
    path("trip/creation/", views.trip_creation, name="trip-creation"),
    path("trip/update/", views.trip_update, name="trip-update"),
    path("trip/list/", views.trip_list, name="trip-list"),
]
