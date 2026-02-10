import backtrader as bt

# Strategy: IV Crush Alpha Strategy 33
# Target Ticker: GOOGL

class IVCrushAlphaStrategy33(bt.Strategy):
    params = (
        ('ticker', 'GOOGL'),
        ('IV_Rank_Min_value', 85),
        ('Post_Earnings_Window_value', 1),
        ('Profit_Target_value', 0.3),
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
