from django.core.validators import RegexValidator, EmailValidator, URLValidator
from django.db import models

from experience.models import Skill, Technology  # type: ignore


class BasePageContent(models.Model):
    FIRST_NAME_VERBOSE_NAME = "Name"
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_VERBOSE_NAME = "Surname"
    LAST_NAME_MAX_LENGTH = 30
    NAME_CHARACTERS_PATTERN = r"^[a-zA-Z\s]+$"
    NAME_CHARACTERS_ERROR_MESSAGE = "{} can only contain letters and spaces."
    PROFESSION_VERBOSE_NAME = "Profession"
    PROFESSION_MAX_LENGTH = 70
    CREATED_ON_VERBOSE_NAME = "Creation date"
    UPDATED_ON_VERBOSE_NAME = "Last update"

    first_name = models.CharField(
        verbose_name=FIRST_NAME_VERBOSE_NAME,
        validators=[
            RegexValidator(regex=NAME_CHARACTERS_PATTERN,
                           message=NAME_CHARACTERS_ERROR_MESSAGE.format(FIRST_NAME_VERBOSE_NAME))],
        max_length=FIRST_NAME_MAX_LENGTH,
        null=False,
        blank=False)
    last_name = models.CharField(
        verbose_name=LAST_NAME_VERBOSE_NAME,
        validators=[
            RegexValidator(regex=NAME_CHARACTERS_PATTERN,
                           message=NAME_CHARACTERS_ERROR_MESSAGE.format(LAST_NAME_VERBOSE_NAME))],
        max_length=LAST_NAME_MAX_LENGTH,
        null=False,
        blank=False)
    profession = models.CharField(
        verbose_name=PROFESSION_VERBOSE_NAME,
        max_length=PROFESSION_MAX_LENGTH,
        null=False,
        blank=False)

    created_on = models.DateField(
        verbose_name=CREATED_ON_VERBOSE_NAME,
        auto_now_add=True)

    updated_on = models.DateField(
        verbose_name=UPDATED_ON_VERBOSE_NAME,
        auto_now=True)

    class Meta:
        abstract = True


class HomePageContent(BasePageContent):
    PHONE_NUMBER_VERBOSE_NAME = "Phone"
    EMAIL_VERBOSE_NAME = "Email"
    LOCATION_VERBOSE_NAME = "Location"
    LOCATION_MAX_LENGTH = 100
    INTRODUCTION_VERBOSE_NAME = "Introduction"
    GITHUB_VERBOSE_NAME = "GitHub"
    LINKEDIN_VERBOSE_NAME = "LinkedIn"
    CV_VERBOSE_NAME = "CV"
    CV_UPLOAD_TO = "documents/cv/"

    phone_number = models.CharField(
        verbose_name=PHONE_NUMBER_VERBOSE_NAME,
        null=False,
        blank=False)

    email = models.EmailField(
        verbose_name=EMAIL_VERBOSE_NAME,
        validators=[EmailValidator()],
        null=False,
        blank=False,
        unique=True)

    location = models.CharField(
        verbose_name=LOCATION_VERBOSE_NAME,
        max_length=LOCATION_MAX_LENGTH,
        null=False,
        blank=False)

    introduction = models.TextField(
        verbose_name=INTRODUCTION_VERBOSE_NAME
    )

    github_link = models.URLField(
        verbose_name=GITHUB_VERBOSE_NAME,
        validators=[URLValidator()],
        null=False,
        blank=False)

    linkedin_link = models.URLField(
        verbose_name=LINKEDIN_VERBOSE_NAME,
        validators=[URLValidator()],
        null=False,
        blank=False)

    cv = models.FileField(
        verbose_name=CV_VERBOSE_NAME,
        upload_to=CV_UPLOAD_TO,
        null=False,
        blank=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Home Page"


class AboutPageContent(BasePageContent):
    ABOUT_VERBOSE_NAME = "About"
    TECHNOLOGIES_VERBOSE_NAME = "Technologies"

    about = models.TextField(
        verbose_name=ABOUT_VERBOSE_NAME
    )

    technologies = models.ManyToManyField(
        Technology,
        verbose_name=TECHNOLOGIES_VERBOSE_NAME)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - About Page"
