from django.contrib import admin

from transactions.models import TransactionModel


@admin.register(TransactionModel)
class TransactionModelAdmin(admin.ModelAdmin):
    list_display = ["wallet_sender", 'wallet_recipient', 'total']
