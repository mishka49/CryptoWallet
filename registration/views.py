from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.serializers import UserSerializer
from .services import send_registration_mail


class UserRegistrationView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            print("SERIALIZER:", serializer.validated_data)
            send_registration_mail(serializer.validated_data['email'])
            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.data, status=status.HTTP_409_CONFLICT)


class ConfirmationRegistrationView(APIView):
    pass
