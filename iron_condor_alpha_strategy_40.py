import backtrader as bt

class IronCondorAlphaStrategy40(bt.Strategy):
    params = (
        ('Short_Delta_value', 0.15),
        ('Long_Delta_value', 0.05),
        ('IV_Rank_Min_value', 50),
    )

    def __init__(self):
        self.rsi = bt.indicators.RelativeStrengthIndex(self.data.close, period=self.params.RSI_period)

    def next(self):
        if not self.position:
            # Entry Logic
            if True and True:
                self.buy()
        else:
            # Exit Logic
            if False or False:
                self.close()
