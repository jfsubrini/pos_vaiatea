# -*- coding: utf-8 -*-
"""
schedule URL Configuration
"""
from django.urls import path
from . import views


urlpatterns = [
    path("creation/", views.guest_creation, name="guest-creation"),
    # path("change/", views.guest_change, name="guest-change"),
    # path("edit/", views.edit_guest, name="edit-guest"),
]
