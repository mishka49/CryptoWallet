from wallets.services.wallet_abc import WalletABC
from web3 import Web3


class WalletETH(WalletABC):
    def __init__(self):
        super().__init__()
        self.type="ETH"

    def create_wallet(self, seed):
        connection = Web3()

        account = connection.eth.account.create()
        self.public_key = account.address
        self.private_key = account.key.hex()
        self.seed = seed

    def save_wallet(self, user):
        super().save_wallet(user)

    @staticmethod
    def get_balance(wallet_address):
        balance = Web3.eth.get_balance(wallet_address)
        return balance
