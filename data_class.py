import numpy as np
import pandas as pd

class Data:
    def __init__(self):
        self.prices_data = None
        self.vol_data = None

    # Prices are stored in a csv file ...
    def read_prices_data(self, file_path, file_name):
        df = pd.read_csv(data=file_path + file_name)
        self.prices_data = df

    
    # Implied volatility cotations are stored in a csv file ...
    def read_vol_data(self, file_path, file_name):
        df = pd.read_csv(file_path + file_name, sep=';',
                         dtype={'Symbol': str,
                                'Date': str,
                                'Expiry': str,
                                'Strike': np.float64,
                                'Spot': np.float64,
                                'ImpliedVolatility': np.float64,
                                'ModelPrice': np.float64},
                         parse_dates=['Date', 'Expiry'])
        self.vol_data = df
        
