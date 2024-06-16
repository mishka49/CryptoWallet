from transactions.services.transaction_btc import TransactionBTC
from transactions.services.transaction_eth import TransactionETH
from transactions.services.transaction_type import TransactionType


class TransactionCreator:
    @staticmethod
    def create_transaction(transaction_type: TransactionType):
        match transaction_type:
            case TransactionType.ETH:
                cls = TransactionETH
            case TransactionType.BTC:
                cls = TransactionBTC
            case _:
                raise ValueError("This transactions type is doesn't exist")

        return cls
