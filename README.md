# presso
Event-driven backtest/realtime quantitative trading system for cryptocurrencies.

## Architecture
![Pipeline](data/image/architecture.png)

## Dependencies
    python3.6
    aiohttp
    numpy

## Run
    ./presso_run manifest.json

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
    def _init(self):
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
        self._execute(self._connectors['coinbase_history'], transaction)
```

### Connector
```
from presso.core.abstract.connector import AbstractConnector


class ExampleConnector(AbstractConnector):
    def _init(self):
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
    def _init(self):
        # TODO
        pass

    def onTransaction(self, transaction):
        # TODO
        pass
```
