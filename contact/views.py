from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import FormView
from .forms import ContactForm
from .models import Contact


class ContactFormView(FormView):
    template_name = "contact/contact.html"
    form_class = ContactForm
    success_url = "thanks/"

    def form_valid(self, form):
        name = form.cleaned_data["name"]
        organization = None if form.cleaned_data["organization"] == "" else form.cleaned_data["organization"]
        email = form.cleaned_data["email"]
        message = form.cleaned_data["message"]
        self.request.session["contact_name"] = name
        Contact.objects.create(
            name=name,
            organization=organization,
            email=email,
            message=message)
        form.send_mail()
        return super().form_valid(form)


def thanks(request):
    context = {
        "message": "Thank you for contacting me",
        "contact_name": request.session.get("contact_name")
    }
    return render(request, "contact/thanks.html", context)