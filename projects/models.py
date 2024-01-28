from django.db import models


class Project(models.Model):
    year = models.PositiveIntegerField()
    title = models.CharField(max_length=50)
    description = models.TextField
    build_with = models.CharField(max_length=200)
    project_link = models.URLField
    github_link = models.URLField
