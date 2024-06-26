from django.db.models import Q
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from transactions.repositories import TransactionRepository
from transactions.serializers import TransactionSerializer
from transactions.services.transaction_creator import TransactionCreator

from wallets.repositories import WalletRepository


class TransactionListView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TransactionSerializer

    def get(self, request):
        transactions = TransactionRepository.get_users_transactions(user=request.user)
        serializer = TransactionListView.serializer_class(transactions)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        try:
            print("REQUEST", request.data)

            transaction = TransactionCreator.create_transaction(transaction_type=WalletRepository.get_wallets_type(request.data["wallet_sender"]))
            transaction.send(
                user_sender=request.user,
                wallet_sender=request.data["wallet_sender"],
                addres_wallet_recipient=request.data["address_wallet_recipient"]
            )
        except ValueError:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(status=status.HTTP_200_OK)


class TransactionFilterView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = TransactionSerializer

    def get_queryset(self):
        queryset = TransactionRepository.get_users_transactions(user=self.request.user)

        user_recipient = self.request.query_params.get('user_recipient')
        wallet = self.request.query_params.get('wallet')
        user_sender = self.request.query_params.get('user_sender')

        if user_recipient is not None:
            queryset.filter(user_recipient=user_recipient)

        if wallet is not None:
            queryset.filter(Q(wallet_sender=wallet) | Q(wallet_recipient=wallet))

        if user_sender is not None:
            queryset.filter(user_sender=user_sender)

        return queryset
