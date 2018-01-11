from presso.alpha.printer import PrinterAlpha
from presso.connector.coinbase_history import CoinbaseHistory
from presso.core.abstract.portfolio import AbstractPortfolio
from presso.core.util.constants import OPERATION, TICKER


class SimplePortfolio(AbstractPortfolio):
    def _init(self):
        self.__printer = PrinterAlpha(self)
        self.__coinbase = CoinbaseHistory()

    def onPrinterSignal(self, transaction):
        transaction.operation = OPERATION.LIMIT
        transaction.buy = TICKER.LTC
        transaction.sell = TICKER.USD
        transaction.amout = 22
        transaction.total = 1000
        self._execute(self.__coinbase, transaction)


SimplePortfolio().run()
