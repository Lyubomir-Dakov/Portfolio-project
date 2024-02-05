from django.shortcuts import render
from django.views.generic import ListView

from .models import Work, Education


def experience(request):
    return render(request, "experience/experience.html")


class WorkView(ListView):
    template_name = "experience/partials/work.html"
    model = Work



class EducationView(ListView):
    template_name = "experience/partials/education.html"
    model = Education
