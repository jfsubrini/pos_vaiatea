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
    path("drink/creation/", views.drink_creation, name="drink-creation"),
    path("drink/update/", views.drink_update, name="drink_update"),
    path("drink/list/", views.drink_list, name="drink-list"),
    path("goodies/creation/", views.goodies_creation, name="goodies-creation"),
    path("goodies/update/", views.goodies_update, name="goodies_update"),
    path("goodies/list/", views.goodies_list, name="goodies-list"),
    path("food/creation/", views.food_creation, name="food-creation"),
    path("food/update/", views.food_update, name="food_update"),
    path("food/list/", views.food_list, name="food-list"),
]
