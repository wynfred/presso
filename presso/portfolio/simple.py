from presso.core.abstract.portfolio import AbstractPortfolio
from presso.alpha.printer import PrinterAlpha


class SimplePortfolio(AbstractPortfolio):
    def _init(self):
        self.__printer = PrinterAlpha(self)

    def onPrinterSignal(self, signal):
        print(signal)
