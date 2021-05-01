import sys
import ccxt
from os import path
if len(sys.argv) < 2:
        print("ERROR: Must specify file containing api configuration.")
        print("Optional arguments: 'crossmargin', 'isolatedmargin', 'futures'")
        exit()
if not path.exists(sys.argv[1]):
        print('ERROR: File', sys.argv[1], 'does not exist.')
        exit()
exec(open(sys.argv[1]).read())
if len(sys.argv) > 2 and sys.argv[2] == 'crossmargin':
        binance = ccxt.binance({'options': { 'defaultType': 'margin' }})
        binance.apiKey = my_api_key
        binance.secret = my_api_secret
        crossassets = binance.fetchBalance()['info']
        for asset in crossassets['userAssets']:
                if float(asset['netAsset']) != 0:
                        print(asset['asset'], asset['netAsset'])
        print('totalNetAssetOfBtc:', crossassets['totalNetAssetOfBtc'], 'BTC')
elif len(sys.argv) > 2 and sys.argv[2] == 'isolatedmargin':
        binance = ccxt.binance()
        binance.apiKey = my_api_key
        binance.secret = my_api_secret
        assets = binance.sapi_get_margin_isolated_account()['assets']
        if assets:
                print(assets[0]['baseAsset']['asset'], str(assets[0]['baseAsset']['netAsset'] + ' = ' + assets[0]['baseAsset']['netAssetOfBtc'] + ' BTC').rjust(30))
                print(assets[0]['quoteAsset']['asset'], str(assets[0]['quoteAsset']['netAsset'] + ' BTC').rjust(30))
                print('totalNetAssetOfBtc:', binance.sapi_get_margin_isolated_account()['totalNetAssetOfBtc'], 'BTC')
        else:
                print('totalNetAssetOfBtc: 0 BTC')
elif len(sys.argv) > 2 and sys.argv[2] == 'futures':
        binance = ccxt.binance({'options': { 'defaultType': 'future' }})
        binance.apiKey = my_api_key
        binance.secret = my_api_secret
        print('Futures totalMarginBalance:', '{:,}'.format(round(float(binance.fetchBalance()['info']['totalMarginBalance']),2)), 'USDT')
else:
        binance = ccxt.binance()
        binance.apiKey = my_api_key
        binance.secret = my_api_secret
        print('asset                         total 123456789012345678')
        for key, value in binance.fetchBalance()['total'].items():
                if value != 0.0:
                        print(key.ljust(16), '{0:.18f}'.format(float(value)).rjust(37).rstrip('0').rstrip('.'))
