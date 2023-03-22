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

# Black Scholes closed formulas for vanilla calls and puts from 1973 paper
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

    def put_price(self, S, K, ttm):
        log_sk = np.log(S / K)
        vol_T = self.vol * np.sqrt(ttm)
        
        d1 = (log_sk + (self.rf_rate + (self.vol**2)/2) * ttm) / vol_T
        d2 = d1 - vol_T

        price = K * np.exp(-self.rf_rate * ttm) * N(-d2) - S * N(-d1)

        put_price = [self.underlying, S, K, ttm, d1, d2, price, 0, 0, 0, 0, 0]
        
        self.put_prices.loc[-1] = put_price
        self.put_prices.index = self.put_prices.index + 1
        self.put_prices = self.put_prices.sort_index()
        
        return self.put_prices
   
# Greeks formulas
    def delta(option_type, d1):
        if option_type == 'CALL':
            delta = N(d1)
        elif option_type == 'PUT':
            delta = -N(-d1)
        
        return delta


    def gamma(self, S, K, ttm, d2):
        num = K * np.exp(-self.rf_rate * ttm) * norm.pdf(d2)
        den = S**2 * self.vol * np.sqrt(ttm)
        gamma = num / den

        return gamma


    def vega(S, d1, ttm):
        vega = S * norm.pdf(d1) * np.sqrt(ttm)

        return vega


    def theta(self, option_type, S, K, ttm, d1, d2):
        if option_type == 'CALL':
            a = - (S * norm.pdf(d1) * self.vol) / (2 * np.sqrt(ttm))
            b = - self.rf_rate * K * np.exp(-self.rf_rate * ttm) * N(d2)
            theta = a + b
        elif option_type = 'PUT':
            a = - (S * norm.pdf(d1) * self.vol) / (2 * np.sqrt(ttm))
            b = self.rf_rate * K * np.exp(-self.rf_rate * ttm) * N(-d2)
            theta = a + b
        
        return theta


    def rho(self, option_type, K, ttm, d2):
        if option_type == 'CALL':
            rho = K * ttm * np.exp(-self.rf_rate * ttm) * N(d2)
        elif option_type == 'PUT':
            rho = -K * ttm * np.exp(-self.rf_rate * ttm) * N(-d2)

        return rho


