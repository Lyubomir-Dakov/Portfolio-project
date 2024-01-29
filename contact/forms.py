from django import forms
from django.core.validators import EmailValidator


class ContactForm(forms.Form):
    full_name = forms.CharField(label="Your name", max_length=100, required=False)
    organization = forms.CharField(label="Your organization", max_length=100, required=False)
    email = forms.EmailField(validators=[EmailValidator()], required=True)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)

    def send_mail(self):
        pass
