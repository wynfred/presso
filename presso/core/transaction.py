class Transaction:
    def __init__(self):
        self.tstamp = 0
        self.signal = 0
        self.amount = 0
        self.total = 0
        self.price = 0
        self.buy = None
        self.sell = None
        self.operation = None
        self.status = None
        self.portfolio = None

    def __str__(self):
        return '%f,%f,%f,%f,%f,%s,%s,%s,%s,%s' % (
            self.tstamp,
            self.signal,
            self.amount,
            self.total,
            self.price,
            str(self.buy),
            str(self.sell),
            str(self.operation),
            str(self.status),
            str(self.portfolio))
    