from django.db import models
from wallets.models import WalletModel

from crypto_wallet import settings


class TransactionModel(models.Model):
    wallet_recipient = models.ForeignKey("wallets.WalletModel", related_name='received_transactions', on_delete=models.SET_NULL, null=True, blank=True)
    user_recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='received_transactions', on_delete=models.SET_NULL, null=True)
    user_sender = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='sent_transactions', on_delete=models.SET_NULL, null=True)
    wallet_sender = models.ForeignKey("wallets.WalletModel", related_name='sent_transactions', on_delete=models.SET_NULL, null=True)
    total = models.FloatField()

    def __str__(self):
        return str(self.pk)
