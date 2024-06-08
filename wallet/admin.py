from django.contrib import admin

from wallet.models import WalletModel


@admin.register(WalletModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ['user', 'public_key', 'private_key']
