from datetime import datetime

from presso.core.transaction import Transaction


class AbstractAlpha:
    def __init__(self, portfolio):
        # Check if portfolio has handler function
        callback_name = 'on%sSignal' % self.name
        if hasattr(portfolio, callback_name):
            self._callback = getattr(portfolio, callback_name)
        else:
            raise NotImplementedError('No handler function defined in portfolio')
        self._init()

    def _init(self):
        raise NotImplementedError

    async def _calcSignal(self, data):
        raise NotImplementedError

    @property
    def name(self):
        raise NotImplementedError

    async def onData(self, data):
        signal = int(await self._calcSignal(data))
        # Avoid using python float for signal value
        if signal > 9999 or signal < -9999:
            raise ValueError('Signal value should between +/-9999')
        transaction = Transaction()
        transaction.tstamp = datetime.now().timestamp()
        transaction.signal = signal
        self._callback(transaction)
