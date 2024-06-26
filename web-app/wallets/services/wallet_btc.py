from web3 import Web3

from wallets.services.wallet_abc import WalletABC


class WalletBTC(WalletABC):
    def __init__(self):
        super().__init__()
        self.type = "BTC"

    def create_wallet(self, seed: str) -> None:
        connection = Web3()

        account = connection.eth.account.create()
        self.public_key = account.address
        self.private_key = account.key.hex()
        self.seed = seed

    def save_wallet(self, user):
        super().save_wallet(user)

    def get_balance(self, wallet_address):
        balance = Web3.eth.get_balance(wallet_address)
        return balance
