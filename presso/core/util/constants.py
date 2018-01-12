from enum import Enum


DATA_ROOT_PATH = 'data/history'

MAX_TIMEOUT = 1

STATUS = Enum('STATUS', ('SUCCESS', 'FAIL'))

TICKER = Enum('TICKER', ('USD', 'USDT', 'BTC', 'LTC', 'BCH', 'ETH', 'ADA', 'XEM'))

OPERATION = Enum('OPERATION', ('LIMIT', 'MARKET'))
