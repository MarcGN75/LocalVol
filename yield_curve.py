import pandas as pd

class YieldCurve:
    def __init__(self, tenors, tenors_f, rates):
        self.tenors = tenors
        self.tenors_f = tenors_f
        self.rates = rates
        self.yield_curve = None


    def set_yield_curve_df(self):
        data_dict = {
            'Tenor': self.tenors,
            'TimeToMaturity': self.tenors_f, 
            'Rate': self.rates}
        df = pd.DataFrame(data=data_dict)
        
        self.yield_curve = df


    def apply_bootstrap(self):
        return self.yield_curve

