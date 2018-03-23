import asyncio

from abc import ABC, abstractmethod

from presso.core.util.constants import STATUS


class AbstractPortfolio(ABC):
    def __init__(self, connectors, statistics, config):
        self._connectors = connectors
        self._statistics = statistics
        self._config = config
        self._transactions = []
        self._positions = {}
        self._init()

    def _execute(self, connector, transaction):
        self._transactions.append(transaction)
        task = asyncio.ensure_future(connector.execute(transaction))
        def __callback(_):
            if transaction.status == STATUS.SUCCESS:
                self._positions[transaction.buy] += transaction.amount
                self._positions[transaction.sell] -= transaction.total
                transaction.portfolio = self._positions.copy()
        task.add_done_callback(__callback)

    def runStatistics(self):
        for transaction in self._transactions:
            for _, stat in self._statistics.items():
                stat.onTransaction(transaction)
        for _, stat in self._statistics.items():
            stat.finish()

    @abstractmethod
    def _init(self):
        raise NotImplementedError
