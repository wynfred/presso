from abc import ABC, abstractmethod


class AbstractStatistics(ABC):
    def __init__(self, config):
        self._config = config
        self._init()

    @abstractmethod
    def _init(self):
        raise NotImplementedError

    @abstractmethod
    def onTransaction(self, transaction):
        raise NotImplementedError

    @abstractmethod
    def finish(self):
        raise NotImplementedError
