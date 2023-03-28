import numpy as np

class yield_curve:
    def __init__(self, tenors, rates, ttm_list):
        self.tenors = tenors
        self.ttm = ttm_list
        self.rates = rates
        self.yield_curve = np.array((self.tenors, self.rates))

    def apply_bootstrap(self):
        return self.yield_curve

