import datetime

from django.core.exceptions import ValidationError
from django.db import models


def validate_end_date(start_date, end_date):
    if end_date < start_date:
        raise ValidationError(
            message="End date cannot be earlier than start date.",
            params={'start_date': start_date, 'end_date': end_date},
        )


class BaseAbility(models.Model):
    NAME_MAX_LENGTH = 50

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        null=False,
        blank=False)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ["name"]


class Skill(BaseAbility):
    pass


class Technology(BaseAbility):
    LOGO_SVG_HELP_TEXT = "Paste your SVG code here."

    logo_svg = models.TextField(
        blank=True,
        help_text=LOGO_SVG_HELP_TEXT
    )


class Certificate(BaseAbility):
    link = models.URLField(
        null=True,
        blank=True
    )

    date = models.CharField()


class BaseExperienceContent(models.Model):
    LOCATION_VERBOSE_NAME = "Location"
    LOCATION_MAX_LENGTH = 100
    SKILLS_VERBOSE_NAME = "Skills"
    TECHNOLOGIES_VERBOSE_NAME = "Technologies"
    LOGO_SVG_VERBOSE_NAME = "Logo"
    LOGO_SVG_HELP_TEXT = "Paste your SVG code here."

    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    location = models.CharField(
        verbose_name=LOCATION_VERBOSE_NAME,
        max_length=LOCATION_MAX_LENGTH,
        null=False,
        blank=False
    )
    skills = models.ManyToManyField(
        Skill,
        verbose_name=SKILLS_VERBOSE_NAME,
        blank=True
    )
    technologies = models.ManyToManyField(
        Technology,
        verbose_name=TECHNOLOGIES_VERBOSE_NAME,
        blank=True)

    logo_svg = models.TextField(
        verbose_name=LOGO_SVG_VERBOSE_NAME,
        blank=True,
        help_text=LOGO_SVG_HELP_TEXT)

    def clean(self):
        validate_end_date(self.start_date, self.end_date)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Work(BaseExperienceContent):
    NAME_VERBOSE_NAME = "Company name"
    NAME_MAX_LENGTH = 100
    TITLE_VERBOSE_NAME = "Working position"
    START_DATE_VERBOSE_NAME = "Start work"
    END_DATE_VERBOSE_NAME = "Leave work"
    TITLE_MAX_LENGTH = 100

    name = models.CharField(
        verbose_name=NAME_VERBOSE_NAME,
        max_length=NAME_MAX_LENGTH,
        null=False,
        blank=False)

    title = models.CharField(
        verbose_name=TITLE_VERBOSE_NAME,
        max_length=TITLE_MAX_LENGTH,
        null=False,
        blank=False
    )

    start_date = models.DateField(
        verbose_name=START_DATE_VERBOSE_NAME,
        null=False,
        blank=False
    )
    end_date = models.DateField(
        verbose_name=END_DATE_VERBOSE_NAME,
        null=True,
        blank=True
    )


class Education(BaseExperienceContent):
    NAME_VERBOSE_NAME = "School or university name"
    NAME_MAX_LENGTH = 50
    SPECIALITY_VERBOSE_NAME = "Speciality"
    CERTIFICATES_VERBOSE_NAME = "Certificates"
    START_DATE_VERBOSE_NAME = "Start school or university"
    END_DATE_VERBOSE_NAME = "Graduate"
    SPECIALITY_MAX_LENGTH = 100

    name = models.CharField(
        verbose_name=NAME_VERBOSE_NAME,
        max_length=NAME_MAX_LENGTH,
        null=False,
        blank=False)

    speciality = models.CharField(
        verbose_name=SPECIALITY_VERBOSE_NAME,
        max_length=SPECIALITY_MAX_LENGTH,
        null=False,
        blank=False
    )

    certificates = models.ManyToManyField(
        Certificate,
        verbose_name=CERTIFICATES_VERBOSE_NAME,
        blank=True)

    start_date = models.DateField(
        verbose_name=START_DATE_VERBOSE_NAME,
        null=False,
        blank=False
    )
    end_date = models.DateField(
        verbose_name=END_DATE_VERBOSE_NAME,
        null=True,
        blank=True
    )
