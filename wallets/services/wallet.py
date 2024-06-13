from enum import Enum

from authentication.models import User
from wallets.repositories import WalletRepository
from wallets.services.bitcoin_wallet import BitcoinWallet
from wallets.services.ethereum_wallet import EthereumWallet


class WalletTypes(Enum):
    BTC = 1,
    ETH = 2,


class Wallet():
    def create_wallet(wallet_type: WalletTypes, user: User):
        match wallet_type:
            case "BTC":
                cls = BitcoinWallet()
            case "ETH":
                cls = EthereumWallet()
            case _:
                raise ValueError("incorrect WalletType")

        wallet = cls.generate_wallet()
        WalletRepository.create_wallet(
            user=user,
            public_key=wallet['public_key'],
            private_key=wallet['private_key']
        )
