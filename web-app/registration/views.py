from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.serializers import UserSerializer
from .repositories import UserRepository
from .services import send_registration_mail, is_confirmed_registration

from .templates import registration


class UserRegistrationView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if (user := UserRepository.get_user_by_email(request.data['email'])) is user.exists() and not user.is_active:
            send_registration_mail(user, request.get_host())
            return Response(status=status.HTTP_200_OK)

        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            send_registration_mail(user, request.get_host())
            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_409_CONFLICT)


class UserSendConfirmMailView(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        if (user := UserRepository.get_user_by_email(request.data['email'])) is not None and not user.is_active:
            send_registration_mail(user, request.get_host())
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_409_CONFLICT)


class ConfirmationRegistrationView(APIView):
    permission_classes = (AllowAny,)

    def get(self, request, uid, token):
        if is_confirmed_registration(uid, token):
            return render(request, "registration.confirm.html")
        #     return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_403_FORBIDDEN)
