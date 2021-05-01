import ccxt
bittrex = ccxt.bittrex({'apiKey': 'MY_API_KEY', 'secret': 'MY_API_SECRET', 'enableRateLimit': True})
for key, value in bittrex.fetchBalance()['total'].items():
        if key != 'BTXCRD' and value != 0:
                print(key.ljust(16), '{0:.18f}'.format(value).rjust(37).rstrip('0').rstrip('.'))
