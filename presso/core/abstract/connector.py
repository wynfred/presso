from abc import ABC, abstractmethod


class AbstractConnector(ABC):
    def __init__(self, dataevents, config):
        self._dataevents = dataevents
        self._config = config
        self._init()

    @abstractmethod
    def _init(self):
        raise NotImplementedError

    @abstractmethod
    async def execute(self, transaction):
        raise NotImplementedError
