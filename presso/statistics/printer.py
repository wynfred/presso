from presso.core.abstract.statistics import AbstractStatistics


class PrinterStatistics(AbstractStatistics):
    def _init(self):
        pass

    def onTransaction(self, transaction):
        print(transaction)
