import numpy as np
import pandas as pd

from scipy.stats import norm

N = norm.cdf

class BlackScholes:
    def __init__(self, underlying, spot, strikes, time_to_maturity,
                 rf_rate, const_vol, implied_vol, local_vol):
        self.underlying = underlying
        self.spot = spot
        self.strikes = strikes
        self.time_to_maturity = time_to_maturity
        self.rf_rate = rf_rate
        self.const_vol = const_vol
        self.implied_vol = implied_vol
        self.local_vol = local_vol
        self.call_prices = pd.DataFrame(columns=['Type', 'Strike', 'Volatility', 'd1', 'd2', 'Price'])
        self.put_prices = pd.DataFrame(columns=['Type', 'Strike', 'Volatility', 'd1', 'd2', 'Price'])


# BLACK SCHOLES CLOSED FOMULAS FOR VANILLA OPTIONS FROM 1973 ******************
    def option_price(self, option_type, K, sigma):
        if option_type=='CALL':
            price = self.call_price(K, sigma)
            
            return price
        elif option_type=='PUT':
            price = self.put_price(K, sigma)
            
            return price
        else:
            return 'WRONG TYPE'

# CALLS -----------------------------------------
    def call_price(self, K, sigma):
        log_sk = np.log(self.spot / K)
        sigma2 = (sigma**2)/2
        r_sigma = (self.rf_rate + sigma2) * self.time_to_maturity
        vol_T = sigma * np.sqrt(self.time_to_maturity)
        
        d1 = (log_sk + r_sigma) / vol_T
        d2 = d1 - vol_T

        n1 = N(d1)
        n2 = N(d2)
        price = self.spot * n1 - K * np.exp(-self.rf_rate * self.time_to_maturity) * n2

        return price

# PUTS ------------------------------------------
    def put_price(self, K, sigma):
        log_sk = np.log(self.spot / K)
        vol_T = sigma * np.sqrt(self.time_to_maturity)
        
        d1 = (log_sk + (self.rf_rate + (sigma**2)/2) * self.time_to_maturity) / vol_T
        d2 = d1 - vol_T

        price = K * np.exp(-self.rf_rate * self.time_to_maturity) * N(-d2) - self.spot * N(-d1)

        return price


# Greeks formulas *************************************************************
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
    def gamma(self, K, sigma, d2):
        num = K * np.exp(-self.rf_rate * self.time_to_maturity) * norm.pdf(d2)
        den = self.spot**2 * sigma * np.sqrt(self.time_to_maturity)
        gamma = num / den

        return gamma
    
    def compute_gamma(self):
        self.call_prices['Gamma'] = self.call_prices.apply(lambda x: self.gamma(x['Strike'],
                                                                                x['TimeToMaturity'],
                                                                                x['d2']), axis=1)

## VEGA
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


# COMPUTE IMPLIED VOLATILITY **************************************************
    # Implied volatility computation based on the Newton-Raphson method
    def compute_implied_volatility_NewtonRaphson(self, option_type, K, market_price, max_iter=1000, start_guess=0.5, precision=0.01):
        sigma = start_guess
        for i in range(max_iter):
            option_price = self.option_price(option_type, K, sigma)
            diff = market_price - option_price
            if abs(diff) < precision:
                return sigma
            
        return sigma

    def compute_implied_volatility_iter(self, option_type, K, market_price,
                                        max_iter=10000, start_guess=0.5, precision=0.1):
        sigma = start_guess
        i = 0
        while i < max_iter:
            price = self.option_price(option_type, K, sigma)
            diff = price - market_price
            if abs(diff) < precision:
                return sigma

            if diff > 0:
                sigma -= 0.001
            else:
                sigma += 0.001

            i += 1

        return sigma

    





