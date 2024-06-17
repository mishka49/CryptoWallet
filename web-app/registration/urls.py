from django.urls import path, include

from registration.views import UserRegistrationView, ConfirmationRegistrationView, UserSendConfirmMailView

urlpatterns = [
    path('create/', UserRegistrationView.as_view()),
    path('confirm-email/<str:uid>/<str:token>/', ConfirmationRegistrationView.as_view(), name='confirm_email'),
    path("repeated-send-confirm-email/", UserSendConfirmMailView.as_view(), name='repeated_send'),
]
