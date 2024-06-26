from django.db.models import Q

from authentication.models import User
from transactions.models import TransactionModel
from wallets.repositories import WalletRepository


class TransactionRepository:
    @staticmethod
    def get_users_transactions(user: User):
        return TransactionModel.objects.filter(Q(user_sender__id=user) | Q(user_recipient=user))

    @staticmethod
    def create_transaction(user_sender: User, wallet_sender, wallet_recipient, total):
        Transaction.objects.create(
            user_sender=user_sender,
            wallet_sender = wallet_sender,
            user_recipient = WalletRepository.get_wallets_user(wallet_recipient),
            wallet_recipient = wallet_recipient,
            total = total
        )