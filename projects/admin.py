from django.contrib import admin
from .models import Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ["Base information", {"fields": ["title", "description", "date"]}],
        ["Links", {"fields": ["github_link", "project_link"]}],
        ["Used technologies and images", {"fields": ["technologies", "project_image"]}],
        ["slug", {"fields": ["slug"]}]
    ]
    list_display = ["title", "date"]
    search_fields = ["title"]
