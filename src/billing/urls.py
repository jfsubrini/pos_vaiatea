# -*- coding: utf-8 -*-
"""
stocks URL Configuration
"""
from django.urls import path
from . import views


urlpatterns = [
    path("bill/", views.payment, name="bill"),
    path("bill/list", views.payment_list, name="bill-list"),
]
