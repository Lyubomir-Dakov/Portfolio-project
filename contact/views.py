from django.shortcuts import render
from django.views.generic import FormView
from .forms import ContactForm


class ContactFormView(FormView):
    template_name = "contact/contact.html"
    form_class = ContactForm
    success_url = "/thanks/"

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)
