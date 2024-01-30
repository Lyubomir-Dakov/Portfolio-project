from django.core.validators import EmailValidator
from django.db import models
from django.utils import timezone


class Contact(models.Model):
    NAME_MAX_LENGTH = 100
    ORGANIZATION_MAX_LENGTH = 100
    MESSAGE_MAX_LENGTH = 2000

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        null=False,
        blank=False)
    organization = models.CharField(
        max_length=ORGANIZATION_MAX_LENGTH,
        null=True,
        blank=True)
    email = models.EmailField(
        validators=[EmailValidator()],
        null=False,
        blank=False,
        unique=True)
    message = models.TextField(
        max_length=MESSAGE_MAX_LENGTH,
        null=False,
        blank=False
    )
    date = models.DateField(
        default=timezone.now(),
        null=False,
        blank=False)

    def __str__(self):
        return self.name



