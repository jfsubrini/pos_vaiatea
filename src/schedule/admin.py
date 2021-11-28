from django.contrib import admin
from .models import Guest, Trip


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name")
    ordering = ("last_name",)
    search_fields = ("last_name", "nationality")
