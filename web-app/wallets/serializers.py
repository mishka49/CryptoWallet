from rest_framework import serializers
from web3 import Web3

from wallets.models import WalletModel, WalletTypeModel
from wallets.services.wallet_creator import WalletCreator


class WalletSerializer(serializers.ModelSerializer):
    type_name = serializers.CharField(source='type.name', read_only=True)
    total = serializers.FloatField(default=0)

    class Meta:
        model = WalletModel
        fields = ('id', 'public_key', 'type', 'type_name', "total")


class WalletTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = WalletTypeModel
        fields = ('id','name',)
