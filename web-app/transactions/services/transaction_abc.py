import abc

from wallets.repositories import WalletRepository
from transactions.repositories import TransactionRepository


class TransactionABC(abc.ABC):
    @classmethod
    @abc.abstractmethod
    def send(cls, user_sender, wallet_sender, wallet_recipient, total, seed):
        wallet_recipient = WalletRepository.get_wallet_by_address(wallet_recipient)
        wallet_sender = WalletRepository.get_wallet_by_address(wallet_sender)

        if wallet_recipient is not None and WalletRepository.get_wallet_by_public_key_and_seed(wallet_sender.public_key, seed) is not None:
            TransactionRepository.save_transaction(
                user_sender=user_sender,
                wallet_sender=wallet_sender,
                wallet_recipient=wallet_recipient,
                total=total
            )

