from django.urls import path

from . import views

urlpatterns = [
    path("", views.experience, name="experience"),
    # path("work/", views.WorkView.as_view(), name="work"),
    # path("education/", views.EducationView.as_view(), name="education")
]
