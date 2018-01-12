import numpy

from presso.core.abstract.connector import AbstractConnector
from presso.core.util.constants import DATA_ROOT_PATH, OPERATION, STATUS, TICKER


DATA_PATH = '%s/%s' % (DATA_ROOT_PATH, 'coinbaseUSD_1-min_data_2017-10-20.csv')

class CoinbaseHistory(AbstractConnector):
    _instance = None

    def __getPrice(self, tstamp):
        index = int(tstamp - self.__const) // 60
        return self.__data[index]

    def __init__(self):
        data = numpy.loadtxt(DATA_PATH, delimiter=',')
        self.__const = data[0][0]
        self.__data = [line[7] for line in data]

    async def execute(self, transaction):
        if transaction.operation == OPERATION.MARKET:
            if transaction.amount:
                if transaction.buy == TICKER.BTC and transaction.sell == TICKER.USD:
                    transaction.price = self.__getPrice(transaction.tstamp)
                    transaction.total = transaction.amount * transaction.price
                elif transaction.buy == TICKER.USD and transaction.sell == TICKER.BTC:
                    transaction.price = 1 / self.__getPrice(transaction.tstamp)
                transaction.total = transaction.amount * transaction.price
                transaction.status = STATUS.SUCCESS
