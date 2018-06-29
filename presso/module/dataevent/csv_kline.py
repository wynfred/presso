import numpy

from presso.core.abstract.dataevent import AbstractDataEvent


class CsvKlineDataEvent(AbstractDataEvent):
    def _init(self):
        self.__data = numpy.loadtxt(self._datapath, delimiter=',')

    async def _iter(self):
        for data in self.__data:
            yield data
