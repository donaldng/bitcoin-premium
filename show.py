from pymongo import MongoClient
import datetime

db = MongoClient().bitcoinPremium.rates

forex = [ key for key in db.find_one() if key not in ['_id', 'usd'] ]
print(forex)
for fx in forex:
    print(fx)
    for x in db.find().sort("_id"):
        try:
            if x["usd"] and x[fx]:
                premium = (x[fx] / x["usd"]) - 1
                premium = round(premium * 100, 2)
                print("%s %s%%" % (datetime.datetime.fromtimestamp( int(x["_id"]) + 28800 ).strftime('%Y-%m-%d %H:%M:%S'), premium))
        except:
            pass