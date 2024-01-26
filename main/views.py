from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from .models import HomePageContent, AboutPageContent


class HomeView(View):
    template_name = "main/partials/home.html"

    def get(self, request):
        content = HomePageContent.objects.first()
        return render(request, self.template_name, {"content": content})


class AboutView(View):
    template_name = "main/partials/about.html"

    def get(self, request):
        content = AboutPageContent.objects.first()
        return render(request, self.template_name, {"content": content})
