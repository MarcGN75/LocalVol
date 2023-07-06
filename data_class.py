import pandas as pd

class Data:
    def __init__(self, underlying, price_date=None, maturity_date=None,
                 time_to_maturity=None, data=None):
        self.underlying = underlying
        self.price_date = price_date
        self.maturity_date = maturity_date
        self.time_to_maturity = time_to_maturity
        self.data = data

    def import_option_data_from_csv(self, file_path, file_name):
        full_path = file_path + file_name
        df = pd.read_csv(full_path, sep=';')

        self.data = df
        
        return df


        



