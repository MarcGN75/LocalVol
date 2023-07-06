import eikon as ek
import pandas as pd
import csv

ek.set_app_key('38833b0f2e7f48fda301d77d0919b030239b5dbc')

def get_option_data(ric, start, end):
    try:
        data = ek.get_timeseries(rics=ric,
                                 start_date=str(start),
                                 end_date=str(end),
                                 interval='daily',
                                 fields=['CLOSE'])
    except:
        print('No data for ', ric)
        return None
    
    return data

def get_option_data_all_strikes(rics_dict, maturity, option_type, start, end):
# Prepare the DataFrame
    df = pd.DataFrame()
    df['PRICE_DATE'] = pd.date_range(start=start, end=end).to_list()
    df['OPTION_TYPE'] = [option_type for i in range(len(df))]
    df['MATURITY'] = [maturity for i in range(len(df))]
# Loop through all rics to get the 'Close' price
    for key in rics_dict.keys():
        ric = key
        strike = rics_dict[key][0]
        
        data = get_option_data(ric, start, end)
        df[strike] = data.CLOSE.to_list()
    
    return df


def print_data_to_csv(df, filename, path='C:\\Users\\MarcNogueira\\Documents\\test_csv\\UBS Commodity Index\\'):
    with open(path + filename, 'w') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=';')
        csvfile.close()

    return path + filename

