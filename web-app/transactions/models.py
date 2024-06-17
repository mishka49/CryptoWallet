from django.db import models
from authentication.models import User
from wallets.models import WalletModel


class TransactionModel(models.Model):
    wallet_recipient = models.ForeignKey("WalletModel", on_delete=models.SET_NULL, null=True),
    user_recipient = models.ForeignKey("User", on_delete=models.SET_NULL, null=True),
    user_sender = models.ForeignKey("User", on_delete=models.SET_NULL, null=True),
    wallet_sender = models.ForeignKey("User", on_delete=models.SET_NULL, null=True),
    total = models.FloatField(),

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)