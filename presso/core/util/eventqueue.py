from asyncio import Lock, PriorityQueue, wait_for

from presso.core.util.constants import MAX_TIMEOUT


class EventQueue:
    __queue = None

    def __init__(self):
        self.__locker = {}
        self.__queue = PriorityQueue()

    async def consume(self):
        caller, data = await self.__queue.get()
        wait_for(caller.sendData(data), MAX_TIMEOUT)
        self.__locker[caller].release()

    async def put(self, caller, data):
        if caller not in self.__locker:
            self.__locker[caller] = Lock()
            await self.__locker[caller].acquire()
        self.__queue.put_nowait((data[0], (caller, data)))
        await self.__locker[caller].acquire()

    def remove(self, caller):
        self.__locker.pop(caller)

    @staticmethod
    def getInstance():
        if EventQueue.__queue:
            return EventQueue.__queue
        else:
            EventQueue.__queue = EventQueue()
