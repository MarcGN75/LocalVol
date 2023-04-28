import requests
import pandas as pd

# list=pd.read_csv('list.csv')
# os.chdir('datastockd')

base_req_str = 'https://api.twelvedata.com/options/chain?symbol='

api_key='be6e66596ab64309bb2f8446885d2446'
symbol='APPL'
expiration_date = '2022-05-20'
url = base_req_str + symbol +'&expiration_date=' + expiration_date + '&apikey=' + api_key

col_names = []
try:
    data = requests.get(url).json()
    data = pd.DataFrame(data['meta'])

    data.set_index('Date', inplace=True)
    data.sort_index(inplace=True)
    data.to_csv('C:/Users/MarcNogueira/Documents/data/test.csv')
except Exception as e:
    print(e)
