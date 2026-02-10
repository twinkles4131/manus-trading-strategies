import backtrader as bt

class CalendarSpreadAlphaStrategy27(bt.Strategy):
    params = (
        ('Front_DTE_value', 7),
        ('Back_DTE_value', 30),
        ('IV_Ratio_Min_value', 1.2),
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
