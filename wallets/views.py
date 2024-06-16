from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from wallets.repositories import WalletRepository
from wallets.serializers import WalletSerializer
from wallets.services.wallet_creator import WalletCreator


class WalletsView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = WalletSerializer

    def get(self, request):
        wallets = WalletRepository.get_users_wallets(user=request.user)
        serializer = WalletsView.serializer_class(wallets)
        return Response(serializer.data, status=status.HTTP_200_OK)


class WalletsCreatorView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, wallet_type):
        try:
            wallet = WalletCreator.create_wallet(wallet_type=wallet_type)
            wallet.save_wallet(request.user)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_200_OK)


class WalletsInfoView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, wallet_address):
        pass
