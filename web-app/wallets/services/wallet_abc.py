from abc import ABC, abstractmethod

from wallets.repositories import WalletRepository, WalletTypeRepository


class WalletABC(ABC):
    @abstractmethod
    def __init__(self):
        self.public_key = str()
        self.private_key = str()
        self.seed = str()
        self.type = str()

    @abstractmethod
    def create_wallet(self, seed: str):
        pass

    @abstractmethod
    def save_wallet(self, user):
        WalletRepository.create_wallet(
            user=user,
            public_key=self.public_key,
            private_key=self.private_key,
            seed=self.seed,
            type=WalletTypeRepository.get_type_by_name(self.type)
        )

    @staticmethod
    @abstractmethod
    def get_balance(wallet_address):
        pass
