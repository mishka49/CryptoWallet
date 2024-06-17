from django.db import models

from crypto_wallet import settings


# Create your models here.
class WalletModel(models.Model):
    public_key = models.CharField(max_length=200)
    private_key = models.CharField(max_length=120)
    seed = models.CharField(max_length=750)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)

    class Meta:
        pass

    def __str__(self):
        return str(self.id)
