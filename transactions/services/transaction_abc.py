import abc


class TransactionABC(abc.ABC):
    @staticmethod
    @abc.abstractmethod
    def send(*args, **kwargs):
        pass
