from django.contrib import admin

from wallets.models import WalletModel, WalletTypeModel


@admin.register(WalletModel)
class WalletModelAdmin(admin.ModelAdmin):
    list_display = ["id"]

@admin.register(WalletTypeModel)
class WalletTypeModelAdmin(admin.ModelAdmin):
    list_display = ["name"]