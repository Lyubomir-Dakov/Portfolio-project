from django.shortcuts import render
from django.views.generic import ListView

from .models import Project


class ProjectsView(ListView):
    template_name = "projects/projects.html"
    model = Project
