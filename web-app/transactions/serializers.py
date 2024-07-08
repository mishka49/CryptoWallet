from rest_framework import serializers

from transactions.models import TransactionModel
from authentication.serializers import UserSerializer
from wallets.serializers import WalletSerializer


class TransactionSerializer(serializers.ModelSerializer):
    user_sender = UserSerializer(read_only=True)
    wallet_sender_id = serializers.SerializerMethodField()
    wallet_recipient_id = serializers.SerializerMethodField()



    class Meta:
        model = TransactionModel
        fields = ["id", "user_sender", "wallet_sender", "wallet_recipient", "wallet_sender_id", "wallet_recipient_id", "total"]


    def get_wallet_recipient_id(self, obj):
        return obj.wallet_recipient.public_key

    def get_wallet_sender_id(self, obj):
        return obj.wallet_sender.public_key