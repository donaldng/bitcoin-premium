import gdax

class Gdax():
    
    def __init__(self):
    
        self.client = gdax.PublicClient()

    def historical_prices(self):
        
        # granularity => candle timeframe in seconds
        rate = self.client.get_product_historic_rates('BTC-USD', granularity=3600)

        '''
        RESPONSE:
            0 time bucket start time
            1 low lowest price during the bucket interval
            2 high highest price during the bucket interval
            3 open opening price (first trade) in the bucket interval
            4 close closing price (last trade) in the bucket interval
            5 volume volume of trading activity during the bucket interval
        '''
        return [ [x[0], x[4], "usd" ] for x in rate ]