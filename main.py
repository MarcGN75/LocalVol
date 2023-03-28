from BlackScholes_class import BlackScholes
from data_class import Data
from yield_curve import yield_curve
from tools import create_new_csv

underlying = 'TEST'
rf_rate = 0.04
vol=0.20
file_path = 'C:/Users/MarcNogueira/Documents/data/'
file_name = 'ImpliedvolData.csv'


def main():
# GET IMPLIED VOLATILITY DATA
    my_data = Data()
    my_data.read_vol_data(file_path, file_name)

    time_to_maturity = my_data.vol_data['TimeToMaturity'].loc[0]
    
    print(time_to_maturity)
    print(my_data.vol_data)

# SET ZERO COUPON YIELD CURVE
    tenors = ['1D', '1M', '3M', '6M', '12M']
    rates = [0.04, 0.04, 0.04, 0.04, 0.04]
    zc_curve = yield_curve(tenors, rates)


    BS = BlackScholes(underlying, vol, rf_rate)
    
    for k in range (45, 155, 5):
        call_price = BS.call_price(spot, k, ttm)
    
    BS.compute_delta()
    BS.compute_gamma()
    BS.compute_vega()
    BS.compute_theta()
    BS.compute_rho()

    csv_path = create_new_csv('test_csv_2.csv')
    BS.call_prices.to_csv(csv_path, sep=';', index=False, decimal='.')

if __name__ == '__main__':
    main()
    
    