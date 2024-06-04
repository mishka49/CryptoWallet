from wallet.repositories import WalletRepository
from wallet.services.wallet import WalletABC
from web3 import Web3


class EthereumWallet(WalletABC):
    @staticmethod
    def generate_wallet():
        connection = Web3()

        account = connection.eth.account.create()
        address = account.address
        private_key = account.key.hex()

        return {"public_key": address, "private_key": private_key}

    @staticmethod
    def get_balance():
        pass
