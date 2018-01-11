from presso.core.abstract.connector import AbstractConnector
from presso.core.util.constants import DATA_ROOT_PATH


DATA_PATH = '%s/%s' % (DATA_ROOT_PATH, 'coinbaseUSD_1-min_data_2017-10-20.csv')

class CoinbaseHistory(AbstractConnector):
    _instance = None

    async def execute(self, transaction):
        raise NotImplementedError
