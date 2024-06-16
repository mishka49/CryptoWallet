from wallets.models import WalletModel


class WalletRepository:
    @staticmethod
    def create_wallet(user, public_key: str, private_key: str):
        WalletModel.objects.create(
            public_key=public_key,
            private_key=private_key,
            user=user
        )

    @staticmethod
    def get_users_wallets(user):
        return WalletModel.objects.filter(user=user)
