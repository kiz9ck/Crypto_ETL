import pandas as pd
import schedule
import time
from config import Config
from api import CryptoFetcher
from db import DatabaseHandler
from notification import EmailSender


def get_last_price(db_handler):
    query = """
    SELECT DISTINCT ON (ticker) ticker, price
    FROM market_prices
    ORDER BY ticker, created_at DESC
    """
    try:
        df = pd.read_sql(query, db_handler.engine)
        return dict(zip(df["ticker"], df["price"]))
    except Exception as e:
        print(f"Error fetching last prices: {e}")
        return {}


def job():
    print("--- Start Job ---")

    fetcher = CryptoFetcher(Config.API_URL)
    db = DatabaseHandler(Config.DB_URL)
    notifier = EmailSender()

    # Get last prices from DB
    last_prices = get_last_price(db)

    # Get current prices
    print("Fetching current prices...")
    current_prices = fetcher.get_prices(Config.COINS)

    for coin, detailts in current_prices.items():
        new_price = detailts["usd"]

        if coin in last_prices:
            old_price = last_prices[coin]

            diff_percent = ((new_price - old_price) / old_price) * 100

            if abs(diff_percent) >= Config.ALERT_THRESHOLD:
                notifier.send_alert(coin, old_price, new_price, diff_percent)
        else:
            print(f"{coin}: No previous price found. Current price = {new_price}")
            diff_percent = 0

    # Transform & Load
    db.save_prices(current_prices)

    print("--- End Job ---")


if __name__ == "__main__":
    print("Docker Crypto ETL Service Started (each 30 mins)")
    job()
    schedule.every(30).minutes.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)
