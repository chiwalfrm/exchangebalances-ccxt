import ccxt
coinbase1 = ccxt.coinbase({'apiKey': 'MY_API_KEY', 'secret': 'MY_API_SECRET', 'enableRateLimit': True})
for key, value in coinbase1.fetchBalance()['total'].items():
        if value != 0:
                print(key.ljust(16), '{0:.18f}'.format(value).rjust(37).rstrip('0').rstrip('.'))
