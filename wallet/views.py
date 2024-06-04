from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from wallet.repositories import WalletRepository
from wallet.serializers import WalletSerializer
from wallet.services.wallet_creator import create_wallet


class Wallets(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = WalletSerializer

    def get(self, request):
        wallets = WalletRepository.get_users_wallets(user=request.user)
        serializer = Wallets.serializer_class(wallets)
        return Response(status=status.HTTP_200_OK)

    def post(self, request, wallet_type):
        try:
            create_wallet(wallet_type=wallet_type, user=request.user)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_200_OK)


