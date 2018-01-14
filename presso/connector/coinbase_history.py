import numpy

from presso.core.abstract.connector import AbstractConnector
from presso.core.util.constants import OPERATION, STATUS, TICKER



class CoinbaseHistory(AbstractConnector):
    def _init(self):
        pass

    async def execute(self, transaction):
        if transaction.operation == OPERATION.MARKET:
            if transaction.amount:
                if transaction.buy == TICKER.BTC and transaction.sell == TICKER.USD:
                    transaction.price = self._dataevents['coinbase_history'].getHistory(1)[0]
                    transaction.total = transaction.amount * transaction.price
                elif transaction.buy == TICKER.USD and transaction.sell == TICKER.BTC:
                    transaction.price = 1 / self._dataevents['coinbase_history'].getHistory(1)[0]
                transaction.total = transaction.amount * transaction.price
                transaction.status = STATUS.SUCCESS
