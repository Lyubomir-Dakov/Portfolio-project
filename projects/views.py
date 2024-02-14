from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Project


class ProjectsView(ListView):
    template_name = "projects/projects.html"
    model = Project


class ProjectDetailView(DetailView):
    model = Project
    template_name = "projects/partials/project.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["object_list"] = Project.objects.all()
        return context
