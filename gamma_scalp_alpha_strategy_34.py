import backtrader as bt

# Strategy: Gamma Scalp Alpha Strategy 34
# Target Ticker: SPX

class GammaScalpAlphaStrategy34(bt.Strategy):
    params = (
        ('ticker', 'SPX'),
        ('Rebalance_Threshold_value', 0.1),
        ('Gamma_Target_value', Positive),
        ('Lookback_value', 10),
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
