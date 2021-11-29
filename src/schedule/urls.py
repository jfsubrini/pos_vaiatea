# -*- coding: utf-8 -*-
"""
schedule URL Configuration
"""
from django.contrib import admin
from django.urls import path
# from . import views


urlpatterns = [
    # TODO arriver plus précisement sur la bonne page
    path("guest/creation/", admin.site.urls),
    # TODO arriver plus précisement sur la bonne page
    path("guest/update/", admin.site.urls),
    # TODO arriver plus précisement sur la bonne page
    path("guest/list/", admin.site.urls),
    # TODO arriver plus précisement sur la bonne page
    path("trip/creation/", admin.site.urls),
    # TODO arriver plus précisement sur la bonne page
    path("trip/update/", admin.site.urls),
    # TODO arriver plus précisement sur la bonne page
    path("trip/list/", admin.site.urls),
]
