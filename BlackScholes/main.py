import pandas as pd

from BlackScholes_class import BlackScholes

underlying = 'TEST'
strike = 110
spot = 100
vol = 0.2
rf_rate = 0.05
ttm = 1

def main():
    BS = BlackScholes(underlying, vol, rf_rate)
    
    for k in range (45, 155, 5):
        call_price = BS.call_price(spot, k, 1)
        print(BS.call_prices)
    
    BS.call_prices.to_csv('C:/Users/MarcNogueira/OneDrive - CMG Consulting Group/Documents/test_csv/test.csv', index=True)

if __name__ == '__main__':
    main()
    
    