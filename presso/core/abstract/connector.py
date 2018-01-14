class AbstractConnector:
    def __init__(self, dataevents, config):
        self._dataevents = dataevents
        self._config = config
        self._init()

    def _init(self):
        raise NotImplementedError

    async def execute(self, transaction):
        raise NotImplementedError
