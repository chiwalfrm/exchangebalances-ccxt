import ccxt
coinex = ccxt.coinex({'apiKey': 'MY_API_KEY', 'secret': 'MY_API_SECRET', 'enableRateLimit': True})
wallet = coinex.fetchBalance()['total']
for coin in wallet:
        print(coin.ljust(16), '{0:.18f}'.format(wallet[coin]).rjust(37).rstrip('0').rstrip('.'))
