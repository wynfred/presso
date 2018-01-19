import logging

import aiohttp


LOG = logging.getLogger('presso')

class HttpSession:
    __session = None

    @staticmethod
    def get():
        if not HttpSession.__session:
            HttpSession.__session = aiohttp.ClientSession(raise_for_status=True)
        return HttpSession.__session

IS_REALTIME = True
def isRealtime():
    return IS_REALTIME

def timeframeToSeconds(timeframe):
    return {
        '1m': 60,
        '5m': 300,
        '10m': 600,
        '15m': 900,
        '30m': 1800,
        '1h': 3600,
        '3h': 10800,
        '6h': 21600,
        '12h': 43200,
        '1D': 86400,
        '7D': 604800,
    }[timeframe]
