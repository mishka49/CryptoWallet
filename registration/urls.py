from django.urls import path, include

from registration.views import UserRegistrationView, ConfirmationRegistrationView

urlpatterns = [
    path('create/', UserRegistrationView.as_view()),
    path('confirm/', ConfirmationRegistrationView.as_view),
]