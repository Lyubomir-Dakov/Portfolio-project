from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Work, Education


def experience(request):
    educations = Education.objects.all()
    works = Work.objects.all()
    context = {
        "educations": educations,
        "works": works
    }
    return render(request, "experience/experience.html", context)


class WorkView(DetailView):
    model = Work
    template_name = "experience/partials/work.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['educations'] = Education.objects.all()
        context['works'] = Work.objects.all()
        return context


class EducationView(DetailView):
    model = Education
    template_name = "experience/partials/education.html"
    slug_field = "slug"
    slug_url_kwarg = "slug"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['educations'] = Education.objects.all()
        context['works'] = Work.objects.all()
        return context
