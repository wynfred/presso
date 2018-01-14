class AbstractStatistics:
    def __init__(self, config):
        self._config = config
        self._init()

    def _init(self):
        raise NotImplementedError

    def onTransaction(self, transaction):
        raise NotImplementedError
