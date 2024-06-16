from django.db.models import Q

from authentication.models import User
from transactions.models import TransactionModel


class TransactionRepository:
    @staticmethod
    def get_users_transactions(user: User):
        return TransactionModel.objects.filter(Q(user_sender=user) | Q(user_recipient=user))