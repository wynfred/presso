import asyncio
import json

import numpy

from presso.core.abstract.dataevent import AbstractDataEvent
from presso.core.util import isRealtime, HttpSession, timeframeToSeconds


class BitfinexKlineDataEvent(AbstractDataEvent):
    def _init(self):
        self.__url = '%s/trade:%s:t%s/hist' % (self._datapath,
                                               self._config['time_frame'],
                                               self._config['market'])
        # Bitfinex uses microseconds instead of seconds
        self.__timeframe = timeframeToSeconds(self._config['time_frame']) * 1000
        if isRealtime():
            self._iter = self.__realtime
        else:
            self.__now = self._config['start_time'] * 1000 // self.__timeframe * self.__timeframe
            self.__end_time = self._config['end_time'] * 1000 // self.__timeframe * self.__timeframe
            self._iter = self.__history

    async def __history(self):
        while self.__end_time > self.__now:
            # Batch size of 100
            params = {'start': self.__now,
                      'end': self.__now + self.__timeframe * 100 - 1,
                      'sort': 1}
            async with HttpSession.get().get(self.__url,
                                             params=params,
                                             verify_ssl=False) as resp:
                for tick in json.loads(await resp.text()):
                    while self.__now != tick[0]:
                        yield self.__parse([])
                        self.__now += self.__timeframe
                    yield self.__parse(tick)
                    self.__now += self.__timeframe
            # Server limit
            await asyncio.sleep(6)

    async def __realtime(self):
        last_tstamp = 0
        while True:
            async with HttpSession.get().get(self.__url,
                                             params={'limit': 2},
                                             verify_ssl=False) as resp:
                tick = json.loads(await resp.text())[1]
                if last_tstamp != tick[0]:
                    last_tstamp = tick[0]
                    yield self.__parse(tick)
            await asyncio.sleep(self.__timeframe / 2000)

    def __parse(self, resp):
        # Use history data if candle is missing from server
        if not resp:
            resp = [self.__now] + [self._history[-1][2]] * 4 + [0]
        resp[0] /= 1000
        # Average price
        resp.append((resp[1] + resp[2]) / 2)
        return numpy.array(resp)
