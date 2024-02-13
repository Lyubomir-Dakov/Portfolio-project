from django.urls import path

from . import views

urlpatterns = [
    path("", views.experience, name="experience"),
    path("work/<slug:slug>/", views.WorkView.as_view(), name="work"),
    path("education/<slug:slug>/", views.EducationView.as_view(), name="education")
]
