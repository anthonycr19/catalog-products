from django.core.mail import EmailMessage
from django.conf import settings


class SMTPNotificationService:

    @classmethod
    def send(cls, recipients, subject, message):
        email = EmailMessage(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            recipients,
        )
        email.send()
