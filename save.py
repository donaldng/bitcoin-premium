from pymongo import MongoClient
from rates.gdax import Gdax
from rates.exchange import Exchange

db = MongoClient().bitcoinPremium.rates

exchanges = []
exchanges.append(Gdax())
exchanges.append(Exchange("bithumb", "krw"))
exchanges.append(Exchange("bitflyer", "jpy"))
exchanges.append(Exchange("luno", "myr"))

for ex in exchanges:
    for x in ex.historical_prices():
        time = x[0]
        rate = x[1]
        currency = x[2]
        res = db.update({"_id": time} , {'$set': { currency: rate }} , upsert=True )
