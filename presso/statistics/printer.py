from presso.core.abstract.statistics import AbstractStatistics


class PrinterStatistics(AbstractStatistics):
    def run(self, transactions):
        for trans in transactions:
            print(trans)
