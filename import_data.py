import refinitiv.dataplatform.eikon as ek
import pandas as pd

ek.set_app_key('DEFAULT_CODE_BOOK_APP_KEY')

def get_option_data(ric, start, end):
    '''
    Get The close price for a single option (ric) and a single maturity within a range of dates
    ric: String - The ticker of the underlying
    start: Date - Start date to retrieve data
    end: Date - Last date to retrieve data
    '''
    try:
        data = ek.get_timeseries(rics=ric,
                                 start_date=str(start),
                                 end_date=str(end),
                                 interval="daily",
                                 fields=['CLOSE'])
    except:
        print('No data for ', ric)
    
    return data

def get_option_data_all_strikes(rics_dict, maturity, option_type, start, end):
    '''
    Get the close price for a set of underlyings and a single maturity and concatenate the result in a Pandas DataFrame
    rics_dict: Dictionnary - Storing the list of underlyings for which we want data
    maturity: Date - Options' Expiry
    option_type: String - CALL or PUT
    start: Date - Start date to retrieve data
    end: Date - Last date to retrieve data
    '''
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

def build_smile():
    return True

