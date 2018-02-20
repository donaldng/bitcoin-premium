from pymongo import MongoClient
from rates.gdax import Gdax
from rates.bithumb import Bithumb

db = MongoClient().bitcoinPremium.rates
data = db.find()

forex = [ key for key in db.find_one() if key not in ['_id', 'usd'] ]

for fx in forex:
    print(fx)
    for x in data:
        try:
            if x["usd"] and x[fx]:
                premium = (x[fx] / x["usd"]) - 1
                premium = round(premium * 100, 2)
                print("%s %s%%" % (x["_id"], premium))
        except:
            pass