from presso.core.abstract.statistics import AbstractStatistics
from presso.core.util import LOG


class LoggerStatistics(AbstractStatistics):
    def _init(self):
        pass

    def onTransaction(self, transaction):
        LOG.info(transaction)

    def finish(self):
        pass
