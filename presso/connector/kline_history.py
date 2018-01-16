import numpy

from presso.core.abstract.connector import AbstractConnector
from presso.core.util.constants import OPERATION, STATUS, TICKER



class KlineHistoryConnector(AbstractConnector):
    def _init(self):
        _, self._dataevent = self._dataevents.popitem()
        self._commission = 0.9975

    def __getPrice(self):
        return self._dataevent.getHistory(1)[0][-1]

    async def execute(self, transaction):
        if transaction.operation == OPERATION.MARKET:
            if transaction.buy == TICKER.BTC and transaction.sell == TICKER.USD:
                transaction.price = self.__getPrice()
            elif transaction.buy == TICKER.USD and transaction.sell == TICKER.BTC:
                transaction.price = 1 / self.__getPrice()
            if transaction.total:
                transaction.amount = transaction.total / transaction.price * self._commission
            elif transaction.amount:
                transaction.total = transaction.amount * transaction.price * self._commission
            transaction.status = STATUS.SUCCESS
        else:
            transaction.status = STATUS.FAIL
