from transactions.services.transaction_abc import TransactionABC


class TransactionETH(TransactionABC):
    @classmethod
    def send(cls, user_sender, wallet_sender, wallet_recipient, total, seed):
        super().send(user_sender=user_sender,
                     wallet_sender=wallet_sender,
                     wallet_recipient=wallet_recipient,
                     total=total,
                     seed=seed)
