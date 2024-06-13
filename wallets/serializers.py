from rest_framework import serializers

from wallets.models import WalletModel


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletModel
        fields = ('id', 'public_key')

