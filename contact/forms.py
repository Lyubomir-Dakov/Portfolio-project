from django import forms
from django.core.validators import EmailValidator
from django.core.mail import send_mail


class ContactForm(forms.Form):
    name = forms.CharField(label="Your name", max_length=100, required=True)
    organization = forms.CharField(label="Your organization", max_length=100, required=False)
    email = forms.EmailField(validators=[EmailValidator()], required=True)
    message = forms.CharField(widget=forms.Textarea, max_length=2000)

    @staticmethod
    def send_mail(name, email):
        send_mail(
            "Lyubomir Dakov",
            f"Hello, {name}",
            "lyubomir.valeriev.dakov@gmail.com",
            [email],
            fail_silently=False,
        )
