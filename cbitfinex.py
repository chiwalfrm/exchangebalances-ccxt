import json
import ccxt
import sys
sumwallets = 0
bitfinex = ccxt.bitfinex({'apiKey': 'YOUR_API_KEY', 'secret': 'YOUR_API_SECRET', 'enableRateLimit': True})
print("w / type / currency / amount / unsettled_interest / available")
for my_wallet in bitfinex.fetchBalance()['info']:
        if len(sys.argv) > 1 and sys.argv[1] == 'futures':
                if my_wallet['type'] == 'trading':
                        print("w / " + str(my_wallet['type']).ljust(8) + " / " + str(my_wallet['currency'].ljust(5)) + " / " + str(my_wallet['amount']).ljust(10) + " / X / " + str(my_wallet['available']))
                        sumwallets = sumwallets + float(my_wallet['amount'])
        else:
                if my_wallet['type'] != 'trading':
                        print("w / " + str(my_wallet['type']).ljust(8) + " / " + str(my_wallet['currency'].ljust(5)) + " / " + str(my_wallet['amount']).ljust(10) + " / X / " + str(my_wallet['available']))
                        sumwallets = sumwallets + float(my_wallet['amount'])
if len(sys.argv) > 1 and sys.argv[1] == 'futures':
        print()
        print("p / symbol / status / amount / base / swap / margin_funding_type / pl / profit_loss_percentage / liquidation_price / leverage / id / mts_create / mts_update / type / collateral / collateral_min / meta / timestamp")
        for my_position in bitfinex.private_post_positions():
                print("p / " + str(my_position['symbol']) + " / " + str(my_position['status']) + " / " + str(my_position['amount']) + " / " + str(my_position['base']) + " / " + str(my_position['swap']) + " / X / " + str(my_position['pl']) + " / X / X / X / " + str(my_position['id']) + " / X / X / X / X / X / X / " + str(my_position['timestamp']))
                print()
                print("Balance:", '{0:.18f}'.format(float(my_wallet['amount']) + float(my_position['pl'])).rstrip('0').rstrip('.'))
