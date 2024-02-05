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
    pass


@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    pass
