from datetime import datetime, timedelta

import jwt
from django.contrib.sites.models import Site
from rest_framework.reverse import reverse_lazy
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework_simplejwt.tokens import AccessToken

from CryptoWallet import settings
from notifications.services import send_mail_for_user


def send_registration_mail(user, site_host):
    print("USER:", user)
    confirm_url = generate_confirm_link(user, site_host)

    send_mail_for_user(
        email=user.email,
        title="Confirm registration in CryptoWallet account",
        message="Thank you for registering on our website. "
                "Please click on the link below to confirm your email address and complete the registration process.\n"
                f"Confirm your email address: {confirm_url}\n"
                "If you did not create this account, simply ignore this message. Best regards, CryptoWallet.com"
    )


def generate_confirm_link(user, host):
    payload = {
        "user_id": user.id,
    }

    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    uid = urlsafe_base64_encode(force_bytes(user.pk))

    return f'{host}/registration/confirm-email/{uid}/{token}/'
