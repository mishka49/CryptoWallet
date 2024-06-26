from transactions.services.transaction_abc import TransactionABC


class TransactionBTC(TransactionABC):
    @staticmethod
    def send(*args, **kwargs):
        TransactionRepository.create_transaction()

