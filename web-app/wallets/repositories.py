from wallets.models import WalletModel, WalletTypeModel


class WalletRepository:
    @staticmethod
    def create_wallet(user, public_key: str, private_key: str, seed: str, type: WalletTypeModel):
        WalletModel.objects.create(
            public_key=public_key,
            private_key=private_key,
            user=user,
            seed=seed,
            type=type
        )

    @staticmethod
    def get_users_wallets(user):
        return WalletModel.objects.filter(user=user)

    @staticmethod
    def get_wallet_by_address(public_key):
        return WalletModel.objects.get(public_key=public_key)

    @staticmethod
    def get_wallet_by_seed(seed):
        return WalletModel.objects.get(seed=seed)

    @staticmethod
    def get_wallets_user(public_key):
        return WalletModel.objects.get(public_key=public_key).user

    @staticmethod
    def get_wallets_type(public_key):
        return WalletModel.objects.get(public_key=public_key).type.name


class WalletTypeRepository:
    @staticmethod
    def get_wallets_types():
        return WalletTypeModel.objects.all()

    @staticmethod
    def get_type_by_name(type_name: str):
        return WalletTypeModel.objects.get(name=type_name)
