from BlackScholes_class import BlackScholes
from Dupire_class import LocalVol
from data_class import Data
from yield_curve import YieldCurve
from tools import create_new_csv, find_rate

underlying = 'TEST'
file_path = 'C:/Users/MarcNogueira/Documents/data/'
file_name = 'ImpliedvolData.csv'


def main():
# GET IMPLIED VOLATILITY DATA
    my_data = Data()
    my_data.read_vol_data(file_path, file_name)

    spot = my_data.vol_data['Spot'].loc[0]
    strikes = my_data.vol_data['Strike'].tolist()
    time_to_maturity = my_data.vol_data['TimeToMaturity'].loc[0]
    implied_vol = my_data.vol_data['ImpliedVolatility'].tolist()

# SET ZERO COUPON YIELD CURVE
    tenors = ['1D', '1M', '3M', '6M', '12M']
    tenors_f = [0.003, 0.083, 0.25, 0.50, 1.00]
    rates = [0.04, 0.04, 0.04, 0.04, 0.04]
    zc_curve = YieldCurve(tenors, tenors_f, rates)
    zc_curve.set_yield_curve_df()

    tenor_ind = find_rate(zc_curve.yield_curve, time_to_maturity)
    rf_rate = zc_curve.yield_curve['Rate'].loc[tenor_ind]
    
    const_vol=0.80
# First model that will be used for constant volatility calculus
    BS_const = BlackScholes(underlying,
                            spot,
                            strikes,
                            time_to_maturity,
                            const_vol,
                            None,
                            None,
                            rf_rate)
# Second model that will be used for implied volatility calculus
    BS_implied = BlackScholes(underlying,
                              spot,
                              strikes,
                              time_to_maturity,
                              const_vol,
                              implied_vol,
                              None,
                              rf_rate)
    
    LocalVol = LocalVol(BS_implied)
    local_vol = LocalVol.compute_local_vol(func_type='Dupire')
# Third model using local volatility
    BS_local = BlackScholes(underlying,
                            spot,
                            const_vol,
                            strikes,
                            time_to_maturity,
                            implied_vol,
                            local_vol,
                            rf_rate)

# Compute prices for both models
    for i in range(len(BS_const.strikes)):
        K = BS_const.strikes[i]
        sigma_const = BS_const.const_vol
        sigma_implied = BS_implied.implied_vol[i]
        sigma_local = BS_local.local_vol[i]
        BS_const.call_price(K, sigma_const)
        BS_implied.call_price(K, sigma_implied)
        BS_local.call_price(K, sigma_local)

# Compute greeks for the constant volatility model
    BS_const.compute_delta()
    BS_const.compute_gamma()
    BS_const.compute_vega()
    BS_const.compute_theta()
    BS_const.compute_rho()

    # csv_path = create_new_csv('test_const.csv')
    # BS_const.call_prices.to_csv(csv_path, sep=';', index=False, decimal='.')
    
# Compute greeks for the implied volatility model
    BS_implied.compute_delta()
    BS_implied.compute_gamma()
    BS_implied.compute_vega()
    BS_implied.compute_theta()
    BS_implied.compute_rho()
    
    # csv_path = create_new_csv('test_implied.csv')
    # BS_implied.call_prices.to_csv(csv_path, sep=';', index=False, decimal='.')

# Compute greeks for the implied volatility model
    BS_local.compute_delta()
    BS_local.compute_gamma()
    BS_local.compute_vega()
    BS_local.compute_theta()
    BS_local.compute_rho()
    
    csv_path = create_new_csv('test_local.csv')
    BS_local.call_prices.to_csv(csv_path, sep=';', index=False, decimal='.')

if __name__ == '__main__':
    main()
    
    