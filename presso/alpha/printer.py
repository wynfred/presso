import random 

from presso.core.abstract.alpha import AbstractAlpha
from presso.core.util import LOG


class PrinterAlpha(AbstractAlpha):
    def _init(self):
        pass

    async def _calcSignal(self, data):
        print(data)
        return (random.random() - 0.5) * 2

    @property
    def name(self):
        return 'Printer'
