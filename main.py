class AlertMagentaAlligator(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020, 11, 20)
        self.SetCash(100000)
        self.AddEquity('SBUX', Resolution.Minute)
        self.AddEquity('TSLA', Resolution.Minute)
        self.AddEquity('BAC', Resolution.Minute)

    def OnData(self, data):
        if not self.Portfolio.Invested:
            self.SetHoldings('SBUX', 0.30)
            self.SetHoldings('TSLA', 0.30)
            self.SetHoldings('BAC', 0.30)
