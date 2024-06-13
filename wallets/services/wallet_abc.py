import abc
from abc import ABC, abstractmethod


class WalletABC(ABC):
    @staticmethod
    @abstractmethod
    def get_balance():
        pass

    @staticmethod
    @abstractmethod
    def generate_wallet():
        pass

    @staticmethod
    @abstractmethod
    def generate_seed(self):
        pass
