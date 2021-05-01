import ccxt
bybit = ccxt.bybit({'enableRateLimit': True})
bybit.apiKey = 'YOUR_API_KEY'
bybit.secret = 'YOUR_API_SECRET'
symbols = []
for element in bybit.fetchTickers():
        element = element.replace("USDT", "")
        element = element.replace("USD", "")
        symbols.append(element)
symbols = sorted(list(set(symbols)))
wallet = bybit.fetchBalance()['total']
for coin in wallet:
        if wallet[coin] != 0.0:
                print(coin.ljust(16), '{:.18f}'.format(wallet[coin]).rjust(37).rstrip('0').rstrip('.'))
