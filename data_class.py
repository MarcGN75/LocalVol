from BlackScholes_class import BlackScholes

class Data:
    def __init__(self, underlying, yield_curve):
        self.underlying = underlying
        self.yield_curve = yield_curve
        self.data = {'CALLS': {}, 'PUTS': {}}

    def import_data_from_csv():
        return True

    def build_price_smile():
        return True

    def compute_implied_volatility(self, option_type, strike, maturity_tenor,
                                   start_sigma=0.9, delta_converge=0.001, threshold=0.001, max_iteration=1000):
        market_price = self.data[option_type][maturity_tenor][1].loc[0]
        sigma = start_sigma
        
        if option_type=='CALL':
            implied_price = BlackScholes.call_price(strike, sigma)
            iteration = 1
        elif option_type=='PUT':
            implied_price = BlackScholes.put_price(strike, sigma)
            iteration = 1
        else:
            return 'Wrong option type, please select CALL or PUT'

        if option_type=='CALL':
            while implied_price - market_price > threshold:
                sigma -= delta_converge
                implied_price = BlackScholes.call_price(strike, sigma)
                iteration += 1
                if iteration==max_iteration:
                    break
                return sigma
        elif option_type=='PUT':
            while implied_price - market_price > threshold:
                sigma -= delta_converge
                implied_price = BlackScholes.put_price(strike, sigma)
                iteration += 1
                if iteration==max_iteration:
                    break
                return sigma
        
        return sigma

    def build_implied_volatility_smile():
        return True

