import pandas as pd

from BlackScholes_class import BlackScholes
from tools import create_new_csv

underlying = 'TEST'
spot = 100
vol = 0.2
rf_rate = 0.05
ttm = 1


def main():
    BS = BlackScholes(underlying, vol, rf_rate)
    
    for k in range (45, 155, 5):
        call_price = BS.call_price(spot, k, ttm)
        print(BS.call_prices)
    
    csv_path = create_new_csv('test_csv_1.csv')
    BS.call_prices.to_csv(csv_path, sep=';', index=True)

if __name__ == '__main__':
    main()
    
    