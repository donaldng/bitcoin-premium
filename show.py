from pymongo import MongoClient
from rates.gdax import Gdax
from rates.bithumb import Bithumb
import datetime

db = MongoClient().bitcoinPremium.rates
data = db.find().sort("_id")

forex = [ key for key in db.find_one() if key not in ['_id', 'usd'] ]

for fx in forex:
    print(fx)
    for x in data:
        try:
            if x["usd"] and x[fx]:
                premium = (x[fx] / x["usd"]) - 1
                premium = round(premium * 100, 2)
                print("%s %s%%" % (datetime.datetime.fromtimestamp( int(x["_id"]) + 28800 ).strftime('%Y-%m-%d %H:%M:%S'), premium))
        except:
            pass