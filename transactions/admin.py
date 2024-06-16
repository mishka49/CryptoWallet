from django.contrib import admin

from transactions.models import TransactionModel


@admin.register(TransactionModel)
class TransactionModelAdmin(admin.ModelAdmin):
    list_display = ["user_sender", 'user_recipient', 'total']
