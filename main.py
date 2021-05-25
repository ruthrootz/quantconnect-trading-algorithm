class AlertMagentaAlligator(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2020, 11, 20)
        self.SetCash(100000)
        self.AddEquity('SBUX', Resolution.Minute)
        self.AddEquity('TSLA', Resolution.Minute)
        self.AddEquity('BAC', Resolution.Minute)
        self.sbux = self.AddEquity('SBUX', Resolution.Daily)
        self.tsla = self.AddEquity('TSLA', Resolution.Daily)
        self.bac = self.AddEquity('BAC', Resolution.Daily)
        self.sbuxMomentum = self.MOMP('SBUX', 30, Resolution.Daily)
        self.tslaMomentum = self.MOMP('TSLA', 30, Resolution.Daily)
        self.bacMomentum = self.MOMP('BAC', 30, Resolution.Daily)

    def OnData(self, data):
        if self.IsWarmingUp:
            return
        if not self.Time.weekday() == 1:
            return
        # if self.spyMomentum.Current.Value > self.bondMomentum.Current.Value:
        #     self.Liquidate("BND")
        #     self.SetHoldings("SPY", 1)
        # else:
        #     self.Liquidate("SPY")
        #     self.SetHoldings("BND", 1)
