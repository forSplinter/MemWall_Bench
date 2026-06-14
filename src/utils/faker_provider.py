from faker.providers import BaseProvider
import random

class CustomProvider(BaseProvider):
    tickers =[
        "AAPL",
        "MSFT",
        "GOOGL",
        "AMZN",
        "TSLA",
        "META",
        "NVDA",
        "JPM",
        "XOM",
        "JNJ",
    ]
    order_types = ["BUY", "SELL"]
    statues = ["executed", "pending", "cancelled"]
    
    def ticker(self):
        return self.random_element(self.tickers)

    def order_type(self):
        return self.random_element(self.order_types)

    def status(self):
        return self.random_element(self.statues)

    def quantity(self, min_value=1, max_value=10000):
        return self.random_int(min_value, max_value)

    def stock_price(self, min_value=10.0, max_value=500.0):
        return round(random.uniform(min_value, max_value), 2)
