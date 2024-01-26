from django.db import models


class BasePageContent(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    profession = models.CharField(max_length=50)


    class Meta:
        abstract = True


class HomePageContent(BasePageContent):
    introduction = models.TextField()


class AboutPageContent(BasePageContent):
    about = models.TextField()
