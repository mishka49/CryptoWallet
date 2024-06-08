from django.core.mail import send_mail

from CryptoWallet import settings


def send_mail_for_user(email, title, message):
    send_mail(
        title,
        message,
        settings.EMAIL_HOST_USER,
        [email],
        fail_silently=False,
    )