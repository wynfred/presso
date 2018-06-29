from presso.core.abstract.portfolio import AbstractPortfolio
from presso.core.util.constants import OPERATION, TICKER


class SimplePortfolio(AbstractPortfolio):
    def _init(self):
        self._positions[TICKER.USD] = 100000
        self._positions[TICKER.BTC] = 0

    def onPrinterSignal(self, transaction):
        if transaction.signal > 0 and self._positions[TICKER.USD] > 0:
            transaction.buy = TICKER.BTC
            transaction.sell = TICKER.USD
            transaction.total = self._positions[TICKER.USD] * 0.5
            transaction.operation = OPERATION.MARKET
        elif transaction.signal < 0 and self._positions[TICKER.BTC] > 0:
            transaction.buy = TICKER.USD
            transaction.sell = TICKER.BTC
            transaction.total = self._positions[TICKER.BTC] * 0.5
            transaction.operation = OPERATION.MARKET
        self._execute(self._connectors['kline_history'], transaction)
