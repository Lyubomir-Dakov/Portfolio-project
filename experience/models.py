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


class BaseExperienceContent(models.Model):
    NAME_MAX_LENGTH = 50
    LOCATION_MAX_LENGTH = 100
    LOGO_SVG_HELP_TEXT = "Paste your SVG code here."

    created_on = models.DateField(auto_now_add=True)
    update_on = models.DateField(auto_now=True)

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        null=False,
        blank=False
    )

    start_date = models.DateField(
        null=False,
        blank=False
    )
    end_date = models.DateField(
        null=False,
        blank=False
    )
    location = models.CharField(
        max_length=LOCATION_MAX_LENGTH,
        null=False,
        blank=False
    )
    skills = models.ManyToManyField(
        Skill,
        blank=True
    )
    technologies = models.ManyToManyField(
        Technology,
        blank=True)

    logo_svg = models.TextField(
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
    TITLE_MAX_LENGTH = 100

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        null=False,
        blank=False
    )


class Education(BaseExperienceContent):
    SPECIALITY_MAX_LENGTH = 100

    specialty = models.CharField(
        max_length=SPECIALITY_MAX_LENGTH,
        null=False,
        blank=False
    )

    certificates = models.ManyToManyField(
        Certificate,
        blank=True)
