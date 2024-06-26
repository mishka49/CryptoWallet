from rest_framework import serializers

from transactions.models import TransactionModel
from authentication.serializers import UserSerializer


class TransactionSerializer(serializers.ModelSerializer):
    user_sender = UserSerializer(read_only=True)

    class Meta:
        model = TransactionModel
        fields = ("user_sender", "wallet_sender", "wallet_recipient")
    # extra_kwargs = {'password': {'write_only': True}}
