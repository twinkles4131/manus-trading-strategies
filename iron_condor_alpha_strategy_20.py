import backtrader as bt

# Strategy: Iron Condor Alpha Strategy 20
# Target Ticker: GLD

class IronCondorAlphaStrategy20(bt.Strategy):
    params = (
        ('ticker', 'GLD'),
        ('Short_Delta_value', 0.15),
        ('Long_Delta_value', 0.05),
        ('IV_Rank_Min_value', 50),
    )

    def __init__(self):
        self.dataclose = self.datas[0].close
        self.rsi = bt.indicators.RelativeStrengthIndex(self.dataclose, period=self.params.RSI_period)

    def next(self):
        if not self.position:
            if self.dataclose[0] > self.ema[0] if hasattr(self, 'ema') else True:
                self.buy()
        else:
            if self.rsi[0] > 70 if hasattr(self, 'rsi') else False:
                self.close()
