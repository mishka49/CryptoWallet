from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from wallets.repositories import WalletRepository, WalletTypeRepository
from wallets.serializers import WalletSerializer, WalletTypeSerializer
from wallets.services.wallet_creator import WalletCreator
from wallets.services.wallet_types import WalletTypes


class WalletsView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = WalletSerializer

    def get(self, request):
        wallets = WalletRepository.get_users_wallets(user=request.user)
        serializer = WalletsView.serializer_class(wallets, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class WalletsCreatorView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            wallet = WalletCreator.generate_wallet(wallet_type=request.data["wallet_type"])
            wallet.create_wallet(seed=request.data["seed"])
            wallet.save_wallet(request.user)
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_200_OK)


class WalletTypeView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = WalletTypeSerializer

    def get(self, request):
        types = WalletTypeRepository.get_wallets_types()
        print("TYPES", types)
        serializer = WalletTypeView.serializer_class(types, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class WalletsInfoView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, wallet_address):
        pass
