from .services import send_mail_for_user
from celery_app import app

@app.task
def send_email(email, title, message):
    send_mail_for_user(email, title, message)