from django.contrib import admin
from .models import Skill, Technology, Certificate, Work, Education


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "display_order")
    list_editable = ("display_order",)


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    list_display = ("name", "display_order")
    list_editable = ("display_order",)


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ("name", "link", "display_order")
    list_editable = ("link", "display_order")


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    fieldsets = [
        ["Base information", {"fields": ["name", "logo_svg", "location", "title"]}],
        ["Learned", {"fields": ["technologies", "skills"]}],
        ["Period", {"fields": ["start_date", "end_date"]}],
        ["History records", {"fields": ["created_on", "updated_on"]}],
        ["Slug", {"fields": ["slug"]}]
    ]
    readonly_fields = ["created_on", "updated_on"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    fieldsets = [
        ["Base information", {"fields": ["name", "logo_svg", "location", "speciality"]}],
        ["Learned", {"fields": ["technologies", "skills"]}],
        ["Certificates", {"fields": ["certificates"]}],
        ["Period", {"fields": ["start_date", "end_date"]}],
        ["History records", {"fields": ["created_on", "updated_on"]}],
        ["Slug", {"fields": ["slug"]}]
    ]
    readonly_fields = ["created_on", "updated_on"]
    prepopulated_fields = {"slug": ("name",)}
