from django.http import Http404
from django.shortcuts import render
from django.views.generic import FormView
from utils.utils import send_email_to_user, send_email_to_me  # type: ignore

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
        contact = Contact.objects.create(
            name=name,
            organization=organization,
            email=email,
            message=message)

        send_email_to_user(contact)
        send_email_to_me(contact)
        self.request.session['form_submitted'] = True

        return super().form_valid(form)


def thanks(request):
    if not request.session.get('form_submitted', False):
        # If the form wasn't submitted, raise a 404 or redirect as needed
        raise Http404("Page not found.")
    request.session.pop('form_submitted', None)
    context = {
        "message": "Thank you for contacting me",
        "contact_name": request.session.get("contact_name")
    }
    return render(request, "contact/thanks.html", context)
