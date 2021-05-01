import ccxt
hitbtc = ccxt.hitbtc({'apiKey': 'MY_API_KEY', 'secret': 'MY_API_SECRET', 'enableRateLimit': True})
for element in hitbtc.fetchBalance({'type': 'account'})['info']:
        if element.get('available') != '0':
                balance = float(element.get('available'))
                print("main " + element.get('currency').ljust(11), f'{balance:37.18f}'.rstrip('0').rstrip('.'))
for element in hitbtc.fetchBalance({'type': 'trading'})['info']:
        if element.get('available') != '0':
                balance = float(element.get('available'))
                print("trad " + element.get('currency').ljust(11), f'{balance:37.18f}'.rstrip('0').rstrip('.'))
