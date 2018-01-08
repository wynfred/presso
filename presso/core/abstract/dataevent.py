import asyncio

import numpy

from presso.core.util.eventqueue import EventQueue


class AbstractDataEvent:
    def addAlpha(self, alpha):
        self._alphas.add(alpha)

    def getHistory(self, num=0):
        return self._history[-num:]

    @classmethod
    def getInstance(cls):
        if not cls._instance:
            inst = cls()
            inst._alphas = set()
            inst._history = None
            asyncio.ensure_future(inst._start())
            cls._instance = inst
        return cls._instance

    def sendData(self, data):
        self._saveHistory(data)
        tasks = [alpha.onData(data) for alpha in self._alphas]
        return asyncio.gather(tasks)

    def _saveHistory(self, data):
        if self._history:
            numpy.vstack([self._history, data])
        else:
            self._history = data

    async def _start(self):
        event_queue = EventQueue.getInstance()
        async for data in self._iter():
            # Wait for previous event to be consumed
            await event_queue.put(self, data)
        event_queue.remove(self)

    async def _iter(self):
        raise NotImplementedError
