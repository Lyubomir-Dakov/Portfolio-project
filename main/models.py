from django.core.validators import RegexValidator, EmailValidator, URLValidator
from django.db import models
from django.utils import timezone


class BasePageContent(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MAX_LENGTH = 30
    NAME_CHARACTERS_PATTERN = r"^[a-zA-Z\s]+$"
    NAME_CHARACTERS_ERROR_MESSAGE = "{} name can only contain letters and spaces."

    first_name = models.CharField(
        validators=[
            RegexValidator(regex=NAME_CHARACTERS_PATTERN, message=NAME_CHARACTERS_ERROR_MESSAGE.format("First"))],
        max_length=30,
        null=False,
        blank=False)
    last_name = models.CharField(
        validators=[
            RegexValidator(regex=NAME_CHARACTERS_PATTERN, message=NAME_CHARACTERS_ERROR_MESSAGE.format("Last"))],
        max_length=30,
        null=False,
        blank=False)
    profession = models.CharField(
        max_length=50,
        null=False,
        blank=False)

    creation_date = models.DateField(auto_now_add=True)

    last_update = models.DateField(auto_now=True)

    class Meta:
        abstract = True


class HomePageContent(BasePageContent):
    LOCATION_MAX_LENGTH = 100
    CV_UPLOAD_TO = "files/"

    introduction = models.TextField()
    phone_number = models.CharField(
        null=False,
        blank=False)

    email = models.EmailField(
        validators=[EmailValidator()],
        null=False,
        blank=False,
        unique=True)

    location = models.CharField(
        max_length=LOCATION_MAX_LENGTH,
        null=False,
        blank=False)

    github_link = models.URLField(
        validators=[URLValidator()],
        null=False,
        blank=False)

    linkedin_link = models.URLField(
        validators=[URLValidator()],
        null=False,
        blank=False)

    cv = models.FileField(
        upload_to=CV_UPLOAD_TO,
        null=False,
        blank=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - Home Page"


class AboutPageContent(BasePageContent):
    about = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} - About Page"
