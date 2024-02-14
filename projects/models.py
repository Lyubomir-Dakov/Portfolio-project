from django.core.validators import URLValidator, MinLengthValidator, \
    RegexValidator
from django.db import models
from experience.models import Technology  # type: ignore


class Project(models.Model):
    TITLE_MAX_LENGTH = 50
    TITLE_ALLOWED_CHARACTERS_PATTERN = r"^[a-zA-Z0-9\s\-_]+$"
    TITLE_ALLOWED_CHARACTERS_ERROR_MESSAGE = "Title can only contain letters, numbers, spaces, hyphens, and underscores."
    DESCRIPTION_MIN_LENGTH = 50
    DESCRIPTION_MIN_LENGTH_ERROR_MESSAGE = "Project description should be at least 50 characters long."
    DESCRIPTION_MAX_LENGTH = 2500
    TECHNOLOGIES_VERBOSE_NAME = "Technologies"
    PROJECT_LINK_MIN_LENGTH = 7
    PROJECT_LINK_MIN_LENGTH_ERROR_MESSAGE = "Project link must be at least 7 characters long."
    GITHUB_LINK_MIN_LENGTH = 7
    GITHUB_LINK_MIN_LENGTH_ERROR_MESSAGE = "GitHub link must be at least 7 characters long."
    PROJECT_IMAGE_UPLOAD_TO = "images/projects/"

    date = models.DateField(
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
    technologies = models.ManyToManyField(
        Technology,
        verbose_name=TECHNOLOGIES_VERBOSE_NAME,
        blank=True)
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

    project_image = models.ImageField(
        upload_to=PROJECT_IMAGE_UPLOAD_TO,
        null=True,
        blank=True
    )

    slug = models.SlugField(
        default="",
        null=False)

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return self.title
