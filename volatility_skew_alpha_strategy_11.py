import backtrader as bt

# Strategy: Volatility Skew Alpha Strategy 11
# Target Ticker: IWM

class VolatilitySkewAlphaStrategy11(bt.Strategy):
    params = (
        ('ticker', 'IWM'),
        ('Skew_Threshold_value', 0.15),
        ('Lookback_value', 20),
        ('Delta_Target_value', 0.25),
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
