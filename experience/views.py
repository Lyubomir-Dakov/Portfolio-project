from django.shortcuts import render
from django.views.generic import ListView

from .models import Work, Education


def experience(request):
    educations = Education.objects.all()
    works = Work.objects.all()
    context = {
            "educations": educations,
            "works": works
        }
    return render(request, "experience/experience.html", context)


class WorkView(ListView):
    template_name = "experience/partials/work.html"
    model = Work


class EducationView(ListView):
    template_name = "experience/partials/education.html"
    model = Education
