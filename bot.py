import logging
from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException
import datetime
from binance.enums import FUTURE_ORDER_TYPE_STOP, TIME_IN_FORCE_GTC
from binance.enums import (
    SIDE_BUY, SIDE_SELL,
    FUTURE_ORDER_TYPE_MARKET,
    FUTURE_ORDER_TYPE_STOP,        
    TIME_IN_FORCE_GTC              
)


logging.basicConfig(
    filename='trading_bot.log',
    level=logging.INFO,
    format='%(asctime)s:%(levelname)s:%(message)s'
)

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)

        if testnet:
            self.client.FUTURES_URL = 'https://testnet.binancefuture.com/fapi'
            self.client.API_URL = 'https://testnet.binancefuture.com'

        logging.info("Bot initialized with testnet = %s", testnet)

    def place_stop_limit_order(self, symbol, side, quantity, price, stop_price):
        """
        Place a stop-limit order:
        - stop_price: when this is reached, limit order is placed at 'price'
        """
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=FUTURE_ORDER_TYPE_STOP,
                quantity=quantity,
                price=price,
                stopPrice=stop_price,
                timeInForce=TIME_IN_FORCE_GTC,
                workingType='MARK_PRICE'
            )
            logging.info(f"Stop-Limit Order Placed: {order}")
            return order
        except BinanceAPIException as e:
            logging.error(f"Stop-Limit Order Error: {e.message}")
            return None


    def get_balance(self, asset='USDT'):
        try:
            balance = self.client.futures_account_balance()
            for b in balance:
                if b['asset'] == asset:
                    logging.info(f"{asset} Balance: {b['balance']}")
                    return float(b['balance'])
        except BinanceAPIException as e:
            logging.error(f"Balance Fetch Error: {e}")
            return None

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type=FUTURE_ORDER_TYPE_MARKET,
                quantity=quantity
            )
            logging.info(f"Market Order Placed: {order}")
            return order
        except BinanceAPIException as e:
            logging.error(f"Order Error: {e.message}")
            return None

    def get_open_orders(self, symbol):
        try:
            orders = self.client.futures_get_open_orders(symbol=symbol)
            logging.info(f"Open Orders: {orders}")
            return orders
        except BinanceAPIException as e:
            logging.error(f"Get Open Orders Error: {e.message}")
            return None
    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
            symbol=symbol,
            side=side,
            type=FUTURE_ORDER_TYPE_LIMIT,
            quantity=quantity,
            price=price,
            timeInForce=TIME_IN_FORCE_GTC )
            logging.info(f"Limit Order Placed: {order}")
            return order
        except BinanceAPIException as e:
            logging.error(f"Limit Order Error: {e.message}")
            return None
if __name__ == "__main__":
  
    API_KEY = "2d22a47ec180fe662f794330efbce6499f0903ad7bd7ae377d560f60e1e523ad"
    API_SECRET = "2e00ae9877089e73a7a4575e53cbbf4e7ccb148e0576e8db75923ef2d707f5f2"

    bot = BasicBot(API_KEY, API_SECRET)

    

    print("=== Binance Futures Testnet Trading Bot ===")
    while True:
        print("\nOptions:")
        print("1. Check Balance")
        print("2. Place Market Order")
        print("3. Place Stop-Limit Order")
        print("4. Place Limit Order")
        print("5. Get Open Orders")
        print("6. Exit")

        choice = input("Enter choice: ").strip()

        if choice == "1":
            asset = input("Enter asset (default USDT): ") or "USDT"
            balance = bot.get_balance(asset)
            print(f"{asset} Balance:", balance)

        elif choice == "2":
            symbol = input("Symbol (e.g. BTCUSDT): ").upper()
            side = input("Side (BUY/SELL): ").upper()
            qty = float(input("Quantity: "))
            result = bot.place_market_order(symbol, SIDE_BUY if side == "BUY" else SIDE_SELL, qty)
            print("Order Result:", result)

        elif choice == "3":
            symbol = input("Symbol (e.g. BTCUSDT): ").upper()
            side = input("Side (BUY/SELL): ").upper()
            qty = float(input("Quantity: "))
            stop_price = input("Stop Price (trigger): ")
            limit_price = input("Limit Price (actual order): ")
            result = bot.place_stop_limit_order(
                symbol,
                SIDE_BUY if side == "BUY" else SIDE_SELL,
                qty,
                price=limit_price,
                stop_price=stop_price
            )
            print("Stop-Limit Order:", result)

        elif choice == "4":
            symbol = input("Symbol (e.g. BTCUSDT): ").upper()
            side = input("Side (BUY/SELL): ").upper()
            qty = float(input("Quantity: "))
            limit_price = input("Limit Price: ")
            result = bot.place_limit_order(
                symbol,
                SIDE_BUY if side == "BUY" else SIDE_SELL,
                qty,
                price=limit_price
            )
            print("Limit Order:", result)

        elif choice == "5":
            symbol = input("Symbol (e.g. BTCUSDT): ").upper()
            orders = bot.get_open_orders(symbol)
            print("Open Orders:", orders)

        elif choice == "6":
            print("Exiting...")
            break


        else:
            print("Invalid choice. Try again.")
