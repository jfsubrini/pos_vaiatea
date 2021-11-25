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
    path("item/creation/", views.item_creation, name="item-creation"),
    path("item/update/", views.item_update, name="item_update"),
    path("item/list/", views.item_list, name="item-list"),
]
