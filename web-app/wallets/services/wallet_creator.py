from wallets.services.wallet_btc import WalletBTC
from wallets.services.wallet_eth import WalletETH
from wallets.services.wallet_types import WalletTypes


class WalletCreator:
    @staticmethod
    def generate_wallet(wallet_type: WalletTypes):
        match wallet_type:
            case "BTC":
                cls = WalletBTC()
            case "ETH":
                cls = WalletETH()
            case _:
                raise ValueError("incorrect WalletType")

        return cls
