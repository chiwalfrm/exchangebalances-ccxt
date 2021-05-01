import sys
import ccxt
from os import path
if len(sys.argv) < 2:
        print("ERROR: Must specify file containing api configuration.")
        exit()
if not path.exists(sys.argv[1]):
        print('ERROR: File', sys.argv[1], 'does not exist.')
        exit()
exec(open(sys.argv[1]).read())
#pp = pprint.PrettyPrinter(width=41, compact=True)
if my_api_subaccount != '':
        ftx = ccxt.ftx({'apiKey': my_api_key, 'secret': my_api_secret, 'enableRateLimit': True, 'headers': {'FTX-SUBACCOUNT': 'ape', 'hostname': 'ftx.us'}})
else:
        ftx = ccxt.ftx({'apiKey': my_api_key, 'secret': my_api_secret, 'enableRateLimit': True, 'hostname': 'ftx.us'})
for key, value in ftx.fetchBalance()['total'].items():
        if value != 0:
                print(key.ljust(16), '{0:.18f}'.format(value).rjust(37).rstrip('0').rstrip('.'))
