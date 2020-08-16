import quandl
from Config import credentials

quandl.ApiConfig.api_key=credentials.quandl_token
data=quandl.get('WIKI/KO')
print(data)