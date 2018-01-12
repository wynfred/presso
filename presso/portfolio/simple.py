from presso.alpha.printer import PrinterAlpha
from presso.statistics.printer import PrinterStatistics
from presso.connector.coinbase_history import CoinbaseHistory
from presso.core.abstract.portfolio import AbstractPortfolio
from presso.core.util.constants import OPERATION, TICKER


class SimplePortfolio(AbstractPortfolio):
    def _init(self):
        self.__printer = PrinterAlpha(self)
        self.__coinbase = CoinbaseHistory()
        self._statistics.append(PrinterStatistics())
        self._positions[TICKER.USD] = 100000
        self._positions[TICKER.BTC] = 0

    def onPrinterSignal(self, transaction):
        transaction.operation = OPERATION.MARKET
        if transaction.signal > 0:
            transaction.buy = TICKER.BTC
            transaction.sell = TICKER.USD
            transaction.amount = 10
        else:
            transaction.buy = TICKER.USD
            transaction.sell = TICKER.BTC
            transaction.amount = 10000
        self._execute(self.__coinbase, transaction)


SimplePortfolio().run()
