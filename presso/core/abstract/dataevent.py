import asyncio

import numpy

from presso.core.transaction import Transaction
from presso.core.util.eventqueue import EventQueue


class AbstractDataEvent:
    def __init__(self, datapath, config):
        self._datapath = datapath
        self._config = config
        self._alphas = set()
        self._history = None
        asyncio.ensure_future(self._start())
        self._init()

    def addAlpha(self, alpha):
        self._alphas.add(alpha)

    def getHistory(self, num=0):
        return self._history[-num:]

    def sendData(self, data):
        self._saveHistory(data)
        transaction = Transaction()
        transaction.tstamp = data[0]
        tasks = [alpha.onData(transaction, data) for alpha in self._alphas]
        return asyncio.gather(*tasks)

    def _saveHistory(self, data):
        if self._history is None:
            self._history = data
        else:
            numpy.vstack([self._history, data])

    async def _start(self):
        event_queue = EventQueue.getInstance()
        async for data in self._iter():
            # Wait for previous event to be consumed
            await event_queue.put(self, data)
        event_queue.remove(self)

    def _init(self):
        raise NotImplementedError

    async def _iter(self):
        raise NotImplementedError
