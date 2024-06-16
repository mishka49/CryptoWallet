from web3 import Web3

from wallets.services.wallet_abc import WalletABC


class WalletBTC(WalletABC):
    def __init__(self):
        self.public_key, self.private_key = self._create_wallet()

    def _create_wallet(self) -> (str, str):
        connection = Web3()

        account = connection.eth.account.create()
        address = account.address
        private_key = account.key.hex()

        return address, private_key

    def save_wallet(self, user):
        super().save_wallet(user)

    def get_balance(self, wallet_address):
        balance = Web3.eth.get_balance(wallet_address)
        return balance
