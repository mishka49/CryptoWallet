from enum import Enum

from authentication.models import User
from wallet.repositories import WalletRepository
from wallet.services.bitcoin_wallet import BitcoinWallet
from wallet.services.ethereum_wallet import EthereumWallet


class WalletTypes(Enum):
    BTC = 1,
    ETH = 2,


def create_wallet(wallet_type: WalletTypes, user: User):
    wallet = dict()

    match wallet_type:
        case "BTC":
            wallet = BitcoinWallet.generate_wallet()
        case "ETH":
            wallet = EthereumWallet.generate_wallet()
        case _:
            raise ValueError("incorrect WalletType")

    WalletRepository.create_wallet(
        user=user,
        public_key=wallet['public_key'],
        private_key=wallet['private_key']
    )
