from django.contrib import admin
from .models import Skill, Technology, Certificate, Work, Education


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    pass


@admin.register(Technology)
class TechnologyAdmin(admin.ModelAdmin):
    pass


@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    pass


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    fieldsets = [
        ["Base information", {"fields": ["name", "logo_svg", "location", "title"]}],
        ["Learned", {"fields": ["technologies", "skills"]}],
        ["Period", {"fields": ["start_date", "end_date"]}],
        ["History records", {"fields": ["created_on", "updated_on"]}]
    ]
    readonly_fields = ["created_on", "updated_on"]


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    fieldsets = [
        ["Base information", {"fields": ["name", "logo_svg", "location", "speciality"]}],
        ["Learned", {"fields": ["technologies", "skills"]}],
        ["Certificates", {"fields": ["certificates"]}],
        ["Period", {"fields": ["start_date", "end_date"]}],
        ["History records", {"fields": ["created_on", "updated_on"]}]
    ]
    readonly_fields = ["created_on", "updated_on"]
