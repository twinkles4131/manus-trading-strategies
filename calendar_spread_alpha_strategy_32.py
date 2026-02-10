import backtrader as bt

# Strategy: Calendar Spread Alpha Strategy 32
# Target Ticker: NVDA

class CalendarSpreadAlphaStrategy32(bt.Strategy):
    params = (
        ('ticker', 'NVDA'),
        ('Front_DTE_value', 7),
        ('Back_DTE_value', 30),
        ('IV_Ratio_Min_value', 1.2),
    )

    def __init__(self):
        self.dataclose = self.datas[0].close

    def next(self):
        if not self.position:
            if self.dataclose[0] > self.ema[0] if hasattr(self, 'ema') else True:
                self.buy()
        else:
            if self.rsi[0] > 70 if hasattr(self, 'rsi') else False:
                self.close()
