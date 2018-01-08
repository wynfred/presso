import asyncio
import sys

from presso.core.util.eventqueue import EventQueue


class AbstractPortfolio:
    def __init__(self):
        self._transactions = []
        self._statistics = []
        self._init()

    def _execute(self, transaction):
        self._transactions.append(transaction)
        asyncio.ensure_future(transaction.execute(self))

    def _run_statistics(self):
        for stat in self._statistics:
            stat.run(self._transactions)

    def run(self):
        loop = asyncio.get_event_loop()
        # Press ENTER to stop eventloop and run statistics
        loop.add_reader(sys.stdin, loop.stop)
        event_queue = EventQueue.getInstance()
        async def main():
            await asyncio.sleep(1)
            while True:
                await event_queue.consume()
        loop.run_until_complete(main())
        self._run_statistics()

    def _init(self):
        raise NotImplementedError
