import numpy as np
import pandas as pd

from scipy.stats import norm

N = norm.cdf

class BlackScholes:
    def __init__(self, underlying, spot, const_vol, strikes, time_to_maturity, implied_vol, rf_rate):
        self.underlying = underlying
        self.spot = spot
        self.const_vol = const_vol
        self.strikes = strikes
        self.time_to_maturity = time_to_maturity
        self.implied_vol = implied_vol
        self.rf_rate = rf_rate
        self.call_prices = pd.DataFrame(columns=['Type', 'Underlying', 'Spot', 'Strike', 'TimeToMaturity', 'd1',
                                                 'd2', 'Price', 'Delta', 'Gamma', 'Vega', 'Theta', 'Rho'])
        self.put_prices = pd.DataFrame(columns=['Type', 'Underlying', 'Spot', 'Strike', 'TimeToMaturity', 'd1',
                                                 'd2', 'Price', 'Delta', 'Gamma', 'Vega', 'Theta', 'Rho'])

# Black Scholes closed formulas for vanilla calls and puts from 1973 paper
    def call_price(self, K):
        log_sk = np.log(self.spot / K)
        vol_T = self.const_vol * np.sqrt(self.time_to_maturity)
        
        d1 = (log_sk + (self.rf_rate + (self.vol**2)/2) * self.time_to_maturity) / vol_T
        d2 = d1 - vol_T

        price = self.spot * N(d1) - K * np.exp(-self.rf_rate * self.time_to_maturity) * N(d2)

        call_price = ['CALL', self.underlying, self.spot, K, self.time_to_maturity, d1, d2, price, 0, 0, 0, 0, 0]
        
        self.call_prices.loc[-1] = call_price
        self.call_prices.index = self.call_prices.index + 1
        self.call_prices = self.call_prices.sort_index()
        
        return self.call_prices

    def put_price(self, K):
        log_sk = np.log(self.spot / K)
        vol_T = self.const_vol * np.sqrt(self.time_to_maturity)
        
        d1 = (log_sk + (self.rf_rate + (self.const_vol**2)/2) * self.time_to_maturity) / vol_T
        d2 = d1 - vol_T

        price = K * np.exp(-self.rf_rate * self.time_to_maturity) * N(-d2) - self.spot * N(-d1)

        put_price = ['PUT', self.underlying, self.spot, K, self.time_to_maturity, d1, d2, price, 0, 0, 0, 0, 0]
        
        self.put_prices.loc[-1] = put_price
        self.put_prices.index = self.put_prices.index + 1
        self.put_prices = self.put_prices.sort_index()
        
        return self.put_prices
   
# Greeks formulas
## DELTA
    @staticmethod
    def delta(option_type, d1):
        if option_type == 'CALL':
            delta = N(d1)
        elif option_type == 'PUT':
            delta = -N(-d1)
        
        return delta

    def compute_delta(self):
        self.call_prices['Delta'] = self.call_prices.apply(lambda x: self.delta(x['Type'],
                                                                                x['d1']), axis=1)

## GAMMA
    def gamma(self, K, d2):
        num = K * np.exp(-self.rf_rate * self.time_to_maturity) * norm.pdf(d2)
        den = self.spot**2 * self.vol * np.sqrt(self.time_to_maturity)
        gamma = num / den

        return gamma
    
    def compute_gamma(self):
        self.call_prices['Gamma'] = self.call_prices.apply(lambda x: self.gamma(x['Strike'],
                                                                                x['d2']), axis=1)

## VEGA
    @staticmethod
    def vega(self, d1):
        vega = self.spot * norm.pdf(d1) * np.sqrt(self.time_to_maturity)

        return vega
    
    def compute_vega(self):
        self.call_prices['Vega'] = self.call_prices.apply(lambda x: self.vega(x['d1']), axis=1)

## THETA
    def theta(self, option_type, K, d1, d2):
        if option_type == 'CALL':
            a = - (self.spot * norm.pdf(d1) * self.const_vol) / (2 * np.sqrt(self.time_to_maturity))
            b = - self.rf_rate * K * np.exp(-self.rf_rate * self.time_to_maturity) * N(d2)
            theta = a + b
        elif option_type == 'PUT':
            a = - (self.spot * norm.pdf(d1) * self.const_vol) / (2 * np.sqrt(self.time_to_maturity))
            b = self.rf_rate * K * np.exp(-self.rf_rate * self.time_to_maturity) * N(-d2)
            theta = a + b
        
        return theta

    def compute_theta(self):
        self.call_prices['Theta'] = self.call_prices.apply(lambda x: self.theta(x['Type'],
                                                                                x['Strike'],
                                                                                x['d1'],
                                                                                x['d2']), axis=1)

## RHO
    def rho(self, option_type, K, d2):
        if option_type == 'CALL':
            rho = K * self.time_to_maturity * np.exp(-self.rf_rate * self.time_to_maturity) * N(d2)
        elif option_type == 'PUT':
            rho = -K * self.time_to_maturity * np.exp(-self.rf_rate * self.time_to_maturity) * N(-d2)

        return rho

    def compute_rho(self):
        self.call_prices['Rho'] = self.call_prices.apply(lambda x: self.rho(x['Type'],
                                                                            x['Strike'],
                                                                            x['d2']), axis=1)


