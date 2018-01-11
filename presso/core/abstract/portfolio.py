import asyncio
import sys

from presso.core.util.constants import STATUS
from presso.core.util.eventqueue import EventQueue


class AbstractPortfolio:
    def __init__(self):
        self._transactions = []
        self._statistics = []
        self._positions = {}
        self._init()

    def _execute(self, connector, transaction):
        self._transactions.append(transaction)
        task = asyncio.ensure_future(connector.execute(transaction))
        def __callback():
            if transaction.status == STATUS.SUCCESS:
                self._positions[transaction.buy] += transaction.amount
                self._positions[transaction.sell] -= transaction.total
                transaction.portfolio = self._positions.copy()
        task.add_done_callback(__callback)

    def _run_statistics(self):
        for stat in self._statistics:
            stat.run(self._transactions)

    def run(self):
        loop = asyncio.get_event_loop()
        # Press ENTER to stop eventloop and run statistics
        loop.add_reader(sys.stdin, loop.stop)
        event_queue = EventQueue.getInstance()
        async def main():
            # Let Dataevents to run first
            await asyncio.sleep(1)
            while True:
                await event_queue.consume()
        loop.run_until_complete(main())
        self._run_statistics()

    def _init(self):
        raise NotImplementedError
