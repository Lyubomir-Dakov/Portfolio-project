from django.core.exceptions import ValidationError
from django.test import TestCase
from .models import Project
from django.utils import timezone
from django.urls import reverse
import datetime

class ProjectModelTests(TestCase):
    YEAR = timezone.now().year
    TITLE = "Test project"
    DESCRIPTION = "This is description for test project. It is very short and simple."
    BUILD_WITH = "Python, Django"
    PROJECT_LINK = "https://www.project_test_link.com"
    GITHUB_LINK = "https://www.github_test_link.com"

    def test_create_project_with_future_year(self):
        """
        Throws ValidationError when the year is higher than the current year
        """

        # self.assertRaises(Project(
        #     year=self.YEAR + 1,
        #     title=self.TITLE,
        #     description=self.DESCRIPTION,
        #     build_with=self.BUILD_WITH,
        #     project_link=self.PROJECT_LINK,
        #     github_link=self.GITHUB_LINK
        # ), ValidationError(f"Choose valid year less than or equal to {self.YEAR}"))

        print(Project.objects.create(
            year=self.YEAR + 1,
            title=self.TITLE,
            description=self.DESCRIPTION,
            build_with=self.BUILD_WITH,
            project_link=self.PROJECT_LINK,
            github_link=self.GITHUB_LINK
        ))

        self.assertQuerySetEqual(Project.objects.all(), [])
