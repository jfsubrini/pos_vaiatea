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
    path("bar/creation/", views.bar_creation, name="bar-creation"),
    path("bar/update/", views.bar_update, name="bar-update"),
    path("bar/list/", views.bar_list, name="bar-list"),
    path("goodies/creation/", views.goodies_creation, name="goodies-creation"),
    path("goodies/update/", views.goodies_update, name="goodies-update"),
    path("goodies/list/", views.goodies_list, name="goodies-list"),
    path("kitchen/creation/", views.kitchen_creation, name="kitchen-creation"),
    path("kitchen/update/", views.kitchen_update, name="kitchen-update"),
    path("kitchen/list/", views.kitchen_list, name="kitchen-list"),
    path("misc/creation/", views.misc_creation, name="misc-creation"),
    path("misc/update/", views.misc_update, name="misc-update"),
    path("misc/list/", views.misc_list, name="misc-list"),
]
