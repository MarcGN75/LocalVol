import numpy as np

from BlackScholes_class import BlackScholes

# One Dupire model per smile/skew i.e. only one maturity for the moment
class Dupire(BlackScholes):
    def __init__(self, spot, time_to_maturity):
        self.spot = spot
        self.ttm = time_to_maturity
        self.local_vol = None

    def compute_local_vol(self, K, implied_vol):
        '''
        ' Function that computes local volatility for a couple (K, T)
        ' K: Float - Strike
        '''
        F = self.spot * np.exp(self.rf_rate * self.ttm)
        y = np.log(K / F)
    # Total implied variance
        w = implied_vol**2 * self.ttm
    # Dw/Dy: Derivatives ...
        Dw_Dy = 1
        Dw_Dy2 = 1
    # Denominator
        A = (1 - (y / 2 * w) * Dw_Dy)**2
        B = (1/4) * (Dw_Dy**2) * ((1/w) + (1/4))
        C = (1/2) * Dw_Dy2
        D = A - B + C
    # Numerator
        N = implied_vol**2
    
    # Implied volatility
        implied_volatility = N / D

        return implied_volatility

    def compute_loc_vol_function(self):
        local_vol_list = []
        for i in range(len(self.implied_vol)):
            temp_k = self.strikes[i]
            temp_implied_vol = self.implied_vol[i]
            
            local_vol = self.compute_local_vol(temp_k, temp_implied_vol)
            local_vol_list.append(local_vol)

        self.local_vol = local_vol_list
