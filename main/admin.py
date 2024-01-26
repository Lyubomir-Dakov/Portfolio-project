from django.contrib import admin

from .models import HomePageContent, AboutPageContent


@admin.register(HomePageContent)
class HomePageAdmin(admin.ModelAdmin):
    pass


@admin.register(AboutPageContent)
class AboutPageAdmin(admin.ModelAdmin):
    pass
