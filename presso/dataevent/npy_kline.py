import numpy

from presso.core.abstract.dataevent import AbstractDataEvent


class NpyKlineDataEvent(AbstractDataEvent):
    def _init(self):
        self.__data = numpy.load(self._datapath)

    async def _iter(self):
        for data in self.__data:
            yield data
