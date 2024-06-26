import jwt
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from crypto_wallet import settings
from notifications.tasks import send_email
from registration.repositories import UserRepository


def send_registration_mail(user, site_host):
    print("USER:", user)
    confirm_url = generate_confirm_link(user, site_host)

    send_email.delay(
        email=user.email,
        title="Confirm registration in CryptoWallet account",
        message="Thank you for registering on our website. "
                "Please click on the link below to confirm your email address and complete the registration process.\n"
                f"Confirm your email address: {confirm_url}\n"
                "If you did not create this account, simply ignore this message. Best regards, CryptoWallet.com"
    )


def generate_confirm_link(user, host: str):
    payload = {
        "user_id": user.id,
    }

    token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')
    uid = urlsafe_base64_encode(force_bytes(user.pk))

    return f'{host}/registration/confirm-email/{uid}/{token}/'


def is_confirmed_registration(uid, token) -> bool:
    id = urlsafe_base64_decode(uid)
    decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
    user_id = decoded_token['user_id']

    if user_id == int(id):
        user = UserRepository.get_user_by_id(id)
        user.is_active = True
        user.save()
        return True

    return False
