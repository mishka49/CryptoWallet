from notifications.services import send_mail_for_user


def send_registration_mail(email):
    send_mail_for_user(
        email=email,
        title="Confirm registration in CryptoWallet account",
        message="Follow this link %%%% to confirm registration"
    )