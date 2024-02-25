from django.conf import settings
from django.core.mail import send_mail


def str_to_bool(value):
    if value.lower() == 'true':
        return True
    elif value.lower() in 'false':
        return False
    else:
        raise ValueError(f"Cannot convert {value} to boolean.")


def send_email_to_user(contact):
    subject = "Greetings from Lyubomir Dakov"
    message = f"""
    Hello, {contact.name}!
    Thank you for contacting me.

    Best regards
    Lyubomir"""
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [contact.email]
    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=recipient_list
    )


def send_email_to_me(contact):
    personal_email_subject = f"{contact.name} message from https://lyubomir-dakov.com"
    if contact.organization is None:
        personal_email_message = f"""
        {contact.name} has used the contact form in https://lyubomir-dakov.com to connect with you.
        Message:

        {contact.message}

        You can reply to {contact.name} at {contact.email}"""
    else:
        personal_email_message = f"""
        {contact.name} from {contact.organization} has used the contact form in https://lyubomir-dakov.com to connect with you.
        Message:

        {contact.message}

        You can reply to {contact.name} at {contact.email}."""

    send_mail(
        subject=personal_email_subject,
        message=personal_email_message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[settings.PERSONAL_EMAIL],
    )
