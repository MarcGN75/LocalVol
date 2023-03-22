import numpy as np
import pandas as pd

from scipy.stats import norm

N = norm.cdf

class BlackScholes:
    def __init__(self, underlying, vol, rf_rate):
        self.underlying = underlying
        self.vol = vol
        self.rf_rate = rf_rate
        self.call_prices = pd.DataFrame(columns=['Underlying', 'Spot', 'Strike', 'TimeToMaturity', 'd1',
                                                 'd2', 'Price', 'Delta', 'Gamma', 'Vega', 'Theta', 'Rho'])
        self.put_prices = pd.DataFrame(columns=['Underlying', 'Spot', 'Strike', 'TimeToMaturity', 'd1',
                                                 'd2', 'Price', 'Delta', 'Gamma', 'Vega', 'Theta', 'Rho'])

# Black Scholes closed formula from 1973 paper
    def call_price(self, S, K, ttm):
        log_sk = np.log(S / K)
        vol_T = self.vol * np.sqrt(ttm)
        
        d1 = (log_sk + (self.rf_rate + (self.vol**2)/2) * ttm) / vol_T
        d2 = d1 - vol_T

        price = S * N(d1) - K * np.exp(-self.rf_rate * ttm) * N(d2)

        call_price = [self.underlying, S, K, ttm, d1, d2, price, 0, 0, 0, 0, 0]
        
        self.call_prices.loc[-1] = call_price
        self.call_prices.index = self.call_prices.index + 1
        self.call_prices = self.call_prices.sort_index()
        
        return self.call_prices

    def put_price():
        price = 0

        return price
   
# Greeks formulas
    def delta():
        delta = 0
        return delta

    def gamma():
        gamma = 0
        return gamma

    def vega():
        vega = 0
        return vega

    def theta():
        theta = 0
        return theta

    def rho():
        rho = 0
        return rho

