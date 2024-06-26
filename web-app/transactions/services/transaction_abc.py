import abc

from wallets.repositories import WalletRepository
from transactions.repositories import TransactionRepository


class TransactionABC(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def send(user_sender, wallet_sender, address_wallet_recipient, seed):
        print("SEND", seed)
        print()
        wallet_recipient = WalletRepository.get_wallet_by_address(address_wallet_recipient)

        if wallet_recipient.exists() and WalletRepository.get_wallet_by_seed(seed).exists():
            TransactionRepository.create_transaction(
                user_sender=user_sender,
                wallet_sender=wallet_sender,
                wallet_recipient=wallet_recipient,
                total=total
            )

