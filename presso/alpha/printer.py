from presso.core.abstract.alpha import AbstractAlpha
from presso.dataevent.coinbase_history import CoinbaseHistory


class PrinterAlpha(AbstractAlpha):
    def _init(self):
        self.__coinbase_h = CoinbaseHistory.getInstance()
        self.__coinbase_h.addAlpha(self)

    async def _calcSignal(self, data):
        print(data)
        return 0

    @property
    def name(self):
        return 'Printer'
