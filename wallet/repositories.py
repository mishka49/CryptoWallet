from authentication.models import User
from wallet.models import WalletModel
from wallet.services.wallet import WalletABC


class WalletRepository:
    @staticmethod
    def create_wallet(user: User, public_key: str, private_key: str):
        WalletModel.objects.create(
            public_key=public_key,
            private_key=private_key,
            user=user
        )

    @staticmethod
    def get_users_wallets(user: User):
        return WalletModel.objects.filter(user=user)

