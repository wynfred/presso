import numpy

from presso.core.abstract.dataevent import AbstractDataEvent
from presso.core.util.constants import DATA_ROOT_PATH


DATA_PATH = '%s/%s' % (DATA_ROOT_PATH, 'coinbaseUSD_1-min_data_2017-10-20.csv')

class CoinbaseHistory(AbstractDataEvent):
    _instance = None

    def __init__(self):
        self.__data = numpy.loadtxt(DATA_PATH, delimiter=',')

    async def _iter(self):
        for data in self.__data:
            yield data
