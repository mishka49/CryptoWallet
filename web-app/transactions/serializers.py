from rest_framework import serializers

from transactions.models import TransactionModel


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionModel
        fields = "__all__"
        extra_kwargs = {'password': {'write_only': True}}