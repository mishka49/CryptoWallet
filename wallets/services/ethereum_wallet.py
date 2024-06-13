from wallets.services.wallet_abc import WalletABC
from web3 import Web3
import web3


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
        wallet_address = "0x2a647559a6c5dcb76ce1751101449ebbc039b157"  # ваш адрес
        balance = Web3.eth.get_balance(wallet_address)
        print(f"balance of {wallet_address}={balance}")

    @staticmethod
    def generate_seed(self):
        pass
