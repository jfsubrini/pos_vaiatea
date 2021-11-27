# -*- coding: utf-8 -*-
"""
stocks URL Configuration
"""
from django.urls import path
from . import views


urlpatterns = [
    path("order/creation/", views.order_creation, name="order-creation"),
    path("order/update/", views.order_update, name="order-update"),
    path("bill/editing", views.bill_editing, name="bill-editing"),
    path("user/creation/", views.user_creation, name="user-creation"),
    path("user/update/", views.user_update, name="user-update"),
    path("user/list/", views.user_list, name="user-list"),
    path("payment/", views.payment, name="payment"),
    path("payment/list", views.payment_list, name="payment-list"),
]
