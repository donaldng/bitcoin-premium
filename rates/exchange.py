import requests, json

class Exchange():
    
    def __init__(self, name, currency):
        self.currency = currency.upper()
        self.timeframe = 1 # hour
        self.timeframe = 24 # daily
        self.url = "https://min-api.cryptocompare.com/data/histohour?fsym=BTC&tsym=%s&limit=60&aggregate=%s&e=%s" % (self.currency, self.timeframe, name)
        self.forex = self.forexConversion()

    def forexConversion(self):
        return requests.get("https://api.fixer.io/latest?symbols=%s&base=USD" % self.currency).json()["rates"][self.currency]

    def historical_prices(self):
        
        result = requests.get(self.url)
        rate = result.json()["Data"]

        return [ [x["time"], x["close"]/self.forex, self.currency ] for x in rate ]