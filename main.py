from BlackScholes_class import BlackScholes
from data_class import Data


def main():
# GET PRICES DATA
    underlying = 'Eurex DowJones UBS Commodity Index'
    file_path = 'C:/Users/MarcNogueira/Documents/data/Eurex DowJones UBS Commodity Index/'
    file_name = 'Eurex DowJones UBS BASE-2 DEC23 AsOf 23062023.csv'

    # Initialize a Data object to import and store market prices
    my_data = Data(underlying)
    my_data.import_option_data_from_csv(file_path, file_name)

# First version of the model that contain only constant volatility
    # Initialize inputs for the following BlackScholes model
    strikes = my_data.data['STRIKE'].to_list()
    spot = 100
    time_to_maturity = my_data.data['TIME_TO_MATURITY'][0]
    const_vol = 0.80
    rf_rate = 0.01454
    # Initialize the model (constant volatility only)
    BS_model = BlackScholes(underlying,
                            spot,
                            strikes,
                            time_to_maturity,
                            rf_rate,
                            const_vol,
                            None,
                            None)
    # Compute Implied volatility and Add it to Data.data for further calculations
    implied_volatility = []
    for i in range(len(my_data.data)):
        option_type = my_data.data['SMILE_TYPE'][i]
        K = my_data.data['STRIKE'][i]
        market_price = my_data.data['SMILE'][i]

        sigma = BS_model.compute_implied_volatility_iter(option_type, K, market_price, start_guess=0.5)
        implied_volatility.append(sigma)
    my_data.data['IMPLIED_VOLATILITY'] = implied_volatility

    my_data.data.to_clipboard()

    LocalVolatility = LocalVol(BS_model.spot,
                               BS_model.strikes,
                               BS_model.time_to_maturity,
                               BS_model.implied_vol)
    LocalVolatility.compute_local_vol(func_type='Dupire')
    local_vol = LocalVolatility.local_vol

# Compute prices for both models
    for i in range(len(BS_local.strikes)):
        K = BS_local.strikes[i]
        # sigma_const = BS_const.const_vol
        # sigma_implied = BS_implied.implied_vol[i]
        sigma_local = BS_local.local_vol[i]
        # BS_const.call_price(K, sigma_const)
        # BS_implied.call_price(K, sigma_implied)
        BS_local.call_price(K, sigma_local)

# Compute greeks for the constant volatility model
    # BS_const.compute_delta()
    # BS_const.compute_gamma()
    # BS_const.compute_vega()
    # BS_const.compute_theta()
    # BS_const.compute_rho()

    # csv_path = create_new_csv('test_const.csv')
    # BS_const.call_prices.to_csv(csv_path, sep=';', index=False, decimal='.')

if __name__ == '__main__':
    main()
    
    