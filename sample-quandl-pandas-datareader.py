import pandas_datareader.data as web
from Config import credentials

data=web.DataReader('WIKI/KO','quandl' ,api_key=credentials.quandl_token)
print(data)
