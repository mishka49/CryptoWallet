import jwt
from django.utils.http import urlsafe_base64_decode
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework_simplejwt.authentication import JWTAuthentication

from CryptoWallet import settings
from authentication.models import User
from authentication.serializers import UserSerializer
from .services import send_registration_mail


class UserRegistrationView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            send_registration_mail(user, request.get_host())
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_409_CONFLICT)


class UserSendConfirmMailView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        if (user := User.objects.get(email=request.data['email'])) is not None and not user.is_active:
            send_registration_mail(user, request.get_host())
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_409_CONFLICT)


class ConfirmationRegistrationView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, uid, token):
        id = urlsafe_base64_decode(uid)
        decoded_token = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        user_id = decoded_token['user_id']

        if user_id == int(id):
            user = User.objects.get(pk=user_id)
            user.is_active = True
            user.save()
            return Response(status=status.HTTP_200_OK)

        return Response(status=status.HTTP_403_FORBIDDEN)
