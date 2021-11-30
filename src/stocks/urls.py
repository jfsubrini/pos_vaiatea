# -*- coding: utf-8 -*-
"""
stocks URL Configuration
"""
from django.urls import path
from . import views


urlpatterns = [
    path("stock/initial/", views.stock_initial, name="stock-initial"),
    path("stock/final/", views.stock_final, name="stock-final"),
    path("stock/update/", views.stock_update, name="stock-update"),
    path("stock/list/", views.stock_list, name="stock-list"),
]
