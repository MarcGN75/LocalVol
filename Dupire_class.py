import numpy as np
from scipy.stats import norm

from BlackScholes_class import BlackScholes

# One Dupire model per smile/skew i.e. only one maturity for the moment
class LocalVol(BlackScholes):
    def __init__(self):
        self.local_vol = None

    def compute_local_vol_Dupire(self, K, implied_vol):
        '''
        ' Compute the local volatility according to Dupire's Equation (1993)
        ' K: Float - Strike
        ' implied_vol: Float - Implied volatility
        '''
        d1 = (np.log(self.spot / K) + (1/2) * implied_vol**2) / (implied_vol * np.sqrt(self.time_to_maturity))
        d1_density = norm.pdf(d1)
        theta = (self.spot * d1_density * implied_vol) / (2 * np.sqrt(self.time_to_maturity))
        gamma = d1_density / (self.spot * implied_vol * np.sqrt(self.time_to_maturity))

        local_vol = theta / ((1/2) * (K**2) * gamma)

        return local_vol

    def compute_local_vol_Derman(self, K, implied_vol):
        '''
        ' Compute the local volatility according to the Derman et al. derivation (2006)
        ' K: Float - Strike
        ' implied_vol: Float - Implied volatility
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
    
    # Local volatility
        local_vol = N / D

        return local_vol

    def compute_local_vol_BS(self):
        '''
        ' Compute local volatility from Black Scholes' implied volatility (1973)
        '''
        return True

    def compute_local_vol(self, func_type):
        '''
        ' Compute local volatility for a set of strikes on one maturity i.e. the volatility smile
        ' func_type: String - The function used to compute the local volatility
            ' Dupire
            ' Derman
            ' BS
        '''
        local_vol_list = []
        if func_type=='Dupire':
            for i in range(len(self.implied_vol)):
                temp_k = self.strikes[i]
                temp_implied_vol = self.implied_vol[i]
            
                local_vol = self.compute_local_vol_Dupire(temp_k, temp_implied_vol)
                local_vol_list.append(local_vol)
        elif func_type=='Derman':
            for i in range(len(self.implied_vol)):
                temp_k = self.strikes[i]
                temp_implied_vol = self.implied_vol[i]
            
                local_vol = self.compute_local_vol_Derman(temp_k, temp_implied_vol)
                local_vol_list.append(local_vol)
        elif func_type=='BS':
            for i in range(len(self.implied_vol)):
                temp_k = self.strikes[i]
                temp_implied_vol = self.implied_vol[i]
            
                local_vol = self.compute_local_vol_BS(temp_k, temp_implied_vol)
                local_vol_list.append(local_vol)

        self.local_vol = local_vol_list

