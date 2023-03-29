from BlackScholes_class import BlackScholes
from data_class import Data
from yield_curve import YieldCurve
from tools import create_new_csv, find_rate

underlying = 'TEST'
vol=0.20
file_path = 'C:/Users/MarcNogueira/Documents/data/'
file_name = 'ImpliedvolData.csv'


def main():
# GET IMPLIED VOLATILITY DATA
    my_data = Data()
    my_data.read_vol_data(file_path, file_name)

    time_to_maturity = my_data.vol_data['TimeToMaturity'].loc[0]
    spot = my_data.vol_data['Spot'].loc[0]

# SET ZERO COUPON YIELD CURVE
    tenors = ['1D', '1M', '3M', '6M', '12M']
    tenors_f = [0.003, 0.083, 0.25, 0.50, 1.00]
    rates = [0.04, 0.04, 0.04, 0.04, 0.04]
    zc_curve = YieldCurve(tenors, tenors_f, rates)
    zc_curve.set_yield_curve_df()

    tenor_ind = find_rate(zc_curve.yield_curve, time_to_maturity)
    rf_rate = zc_curve.yield_curve['Rate'].loc[tenor_ind]

    BS = BlackScholes(underlying, vol, rf_rate)
    
    for k in my_data.vol_data['Strike']:
        implied_vol = 
        BS = BlackScholes(underlying, implied_vol)
        call_price = BS.call_price(spot, k, time_to_maturity)
    
    BS.compute_delta()
    BS.compute_gamma()
    BS.compute_vega()
    BS.compute_theta()
    BS.compute_rho()

    csv_path = create_new_csv('test_csv_2.csv')
    BS.call_prices.to_csv(csv_path, sep=';', index=False, decimal='.')

if __name__ == '__main__':
    main()
    
    