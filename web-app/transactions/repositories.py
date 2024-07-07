from django.db.models import Q

from authentication.models import User
from transactions.models import TransactionModel
from wallets.repositories import WalletRepository


class TransactionRepository:
    @staticmethod
    def get_users_transactions(user: User):
        return TransactionModel.objects.filter(Q(user_sender__id=user.id) | Q(user_recipient=user.id ))

    @staticmethod
    def save_transaction(user_sender: User, wallet_sender, wallet_recipient, total):
        print("WALLeT USER", WalletRepository.get_wallets_user(wallet_recipient.public_key))
        print(user_sender, wallet_sender, wallet_recipient.public_key, total)
        TransactionModel.objects.create(
            user_sender=user_sender,
            wallet_sender=wallet_sender,
            user_recipient=WalletRepository.get_wallets_user(wallet_recipient.public_key),
            wallet_recipient=wallet_recipient,
            total=total
        )