from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    fieldsets = [
        ["Contact", {"fields": ["name", "email"]}],
        ["Additional information", {"fields": ["organization"]}],
        ["Message", {"fields": ["message"]}],
        ["Date", {"fields": ["date"]}]
    ]
    list_display = ["name", "organization", "date"]
    list_filter = ["name", "organization", "date"]
    search_fields = ["name", "organization", "date"]
