import ccxt
bitmex = ccxt.bitmex()
bitmex.apiKey = 'YOUR_API_KEY'
bitmex.secret = 'YOUR_API_SECRET'
print('Futures marginBalance:', bitmex.fetchBalance()['total'].get('BTC'), 'BTC')
