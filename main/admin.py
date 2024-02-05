from django.contrib import admin

from .models import HomePageContent, AboutPageContent


@admin.register(HomePageContent)
class HomePageAdmin(admin.ModelAdmin):
    fieldsets = [
        ["Names", {"fields": ["first_name", "last_name"]}],
        ["Base contacts", {"fields": ["phone_number", "email", "location"]}],
        ["Base information", {"fields": ["profession", "introduction"]}],
        ["Contact links", {"fields": ["linkedin_link", "github_link"]}],
        ["Files", {"fields": ["cv", ]}],
        ["History records", {"fields": ["created_on", "updated_on"]}],
    ]
    readonly_fields = ["created_on", "updated_on"]


@admin.register(AboutPageContent)
class AboutPageAdmin(admin.ModelAdmin):
    fieldsets = [
        ["Names", {"fields": ["first_name", "last_name"]}],
        ["Base information", {"fields": ["profession", "about"]}],
        ["History records", {"fields": ["created_on", "updated_on"]}],
    ]
    readonly_fields = ["created_on", "updated_on"]
