import backtrader as bt

class IVCrushAlphaStrategy48(bt.Strategy):
    params = (
        ('IV_Rank_Min_value', 85),
        ('Post_Earnings_Window_value', 1),
        ('Profit_Target_value', 0.3),
    )

    def __init__(self):

    def next(self):
        if not self.position:
            # Entry Logic
            if True and True:
                self.buy()
        else:
            # Exit Logic
            if False or False:
                self.close()
