from django.core.validators import MaxValueValidator, MinValueValidator, URLValidator, MinLengthValidator, \
    RegexValidator
from django.db import models
from django.utils import timezone


class Project(models.Model):
    YEAR_MIN_VALUE = 2021
    YEAR_MIN_VALUE_ERROR_MESSAGE = "Choose year after 2021."
    YEAR_MAX_VALUE = timezone.now().year
    YEAR_MAX_VALUE_ERROR_MESSAGE = f"Choose valid year less than or equal to {YEAR_MAX_VALUE}"
    TITLE_MAX_LENGTH = 50
    TITLE_ALLOWED_CHARACTERS_PATTERN = r"^[a-zA-Z0-9\s\-_]+$"
    TITLE_ALLOWED_CHARACTERS_ERROR_MESSAGE = "Title can only contain letters, numbers, spaces, hyphens, and underscores."
    DESCRIPTION_MIN_LENGTH = 50
    DESCRIPTION_MIN_LENGTH_ERROR_MESSAGE = "Project description should be at least 50 characters long."
    DESCRIPTION_MAX_LENGTH = 2500
    BUILD_WITH_MAX_LENGTH = 300
    PROJECT_LINK_MIN_LENGTH = 7
    PROJECT_LINK_MIN_LENGTH_ERROR_MESSAGE = "Project link must be at least 7 characters long."
    GITHUB_LINK_MIN_LENGTH = 7
    GITHUB_LINK_MIN_LENGTH_ERROR_MESSAGE = "GitHub link must be at least 7 characters long."

    year = models.PositiveIntegerField(
        validators=[
            MinValueValidator(limit_value=YEAR_MIN_VALUE, message=YEAR_MIN_VALUE_ERROR_MESSAGE),
            MaxValueValidator(limit_value=YEAR_MAX_VALUE, message=YEAR_MAX_VALUE_ERROR_MESSAGE)],
        null=False,
        blank=False)
    title = models.CharField(
        validators=[
            RegexValidator(regex=TITLE_ALLOWED_CHARACTERS_PATTERN, message=TITLE_ALLOWED_CHARACTERS_ERROR_MESSAGE)],
        max_length=TITLE_MAX_LENGTH,
        null=False,
        blank=False)
    description = models.TextField(
        validators=[
            MinLengthValidator(limit_value=DESCRIPTION_MIN_LENGTH, message=DESCRIPTION_MIN_LENGTH_ERROR_MESSAGE)],
        max_length=DESCRIPTION_MAX_LENGTH,
        null=False,
        blank=False)
    build_with = models.CharField(
        max_length=BUILD_WITH_MAX_LENGTH,
        null=False,
        blank=False)
    project_link = models.URLField(
        validators=[
            URLValidator(),
            MinLengthValidator(limit_value=PROJECT_LINK_MIN_LENGTH, message=PROJECT_LINK_MIN_LENGTH_ERROR_MESSAGE)],
        null=True,
        blank=True,
        unique=True)
    github_link = models.URLField(
        validators=[
            URLValidator(),
            MinLengthValidator(limit_value=GITHUB_LINK_MIN_LENGTH, message=GITHUB_LINK_MIN_LENGTH_ERROR_MESSAGE)],
        null=False,
        blank=False,
        unique=True)

    def __str__(self):
        return self.title
