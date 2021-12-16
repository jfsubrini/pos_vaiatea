# -*- coding: utf-8 -*-
"""
stocks URL Configuration
"""
from django.urls import path
from . import pdf_generator


urlpatterns = [
    path('pdfbill/', pdf_generator.pdf_bill, name='generate-pdf-bill-file')
]  # TODO
