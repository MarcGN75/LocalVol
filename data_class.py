import numpy as np
import pandas as np

class Data:
    def __init__(self):
        self.prices_data = None
        self.vol_data = None
        self.rates_data = None

    # Prices are stored in a csv file ...
    def read_prices_data(self, file_path, file_name):
        return self.prices_data
    
    # Implied volatility cotations are stored in a csv file ...
    def read_vol_data(self, file_path, file_name):
        return self.vol_data

    # Zero coupon yield curve is stored in a csv file ...
    def read_rates_data(self, file_path, file_name):
        return self.rates_data
