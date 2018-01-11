class AbstractConnector:
    @classmethod
    def getInstance(cls):
        if not cls._instance:
            cls._instance = cls()
        return cls._instance

    async def execute(self, transaction):
        raise NotImplementedError
