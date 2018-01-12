# presso

## Architecture
![Pipeline](data/image/architecture.png)

## Dependencies
    python3.6
    aiohttp
    numpy

## Run
    python3 your_portfolio.py

## Examples

### Alpha
```
from presso.core.abstract.alpha import AbstractAlpha


class ExampleAlpha(AbstractAlpha):
    def _init(self):
        # TODO
        pass

    async def _calcSignal(self, data):
        # TODO
        pass

    @property
    def name(self):
        return 'Example'
```

### DataEvent
```
from presso.core.abstract.dataevent import AbstractDataEvent


class ExampleDataEvent(AbstractDataEvent):
    _instance = None

    def __init__(self):
        # TODO
        pass

    async def _iter(self):
        # TODO
        pass
```

### Portfolio
```
from presso.core.abstract.portfolio import AbstractPortfolio


class ExamplePortfolio(AbstractPortfolio):
    def _init(self):
        # TODO
        self._positions[TICKER.USD] = 100000
        self._positions[TICKER.BTC] = 0

    def onExampleSignal(self, transaction):
        if transaction.signal > 0:
            # TODO
            transaction.operation = OPERATION.MARKET
            transaction.buy = TICKER.BTC
            transaction.sell = TICKER.USD
            transaction.amount = 10
        self._execute(self.__coinbase, transaction)


ExamplePortfolio().run()
```

### Connector
```
from presso.core.abstract.connector import AbstractConnector


class ExampleConnector(AbstractConnector):
    _instance = None

    def __init__(self):
        # TODO
        pass

    async def execute(self, transaction):
        # TODO
        pass
```

### Statistics
```
from presso.core.abstract.statistics import AbstractStatistics


class ExampleStatistics(AbstractStatistics):
    def run(self, transactions):
        for trans in transactions:
            # TODO
            pass
```
