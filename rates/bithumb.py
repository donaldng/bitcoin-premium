import requests, json

class Bithumb():
    
    def __init__(self):
        self.url = "https://min-api.cryptocompare.com/data/histohour?fsym=BTC&tsym=KRW&limit=60&aggregate=1&e=BITHUMB"
        self.forex = self.forexConversion()

    def forexConversion(self):
        return requests.get("https://api.fixer.io/latest?symbols=KRW&base=USD").json()["rates"]["KRW"]

    def historical_prices(self):
        
        result = requests.get(self.url)
        rate = result.json()["Data"]

        return [ [x["time"], x["close"]/self.forex, "krw" ] for x in rate ]