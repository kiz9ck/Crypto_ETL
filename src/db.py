import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime
from typing import Dict, Any


class DatabaseHandler:
    def __init__(self, connection_url: str):
        self.engine = create_engine(connection_url)

    def save_prices(self, raw_data: Dict[str, Any]):
        if not raw_data:
            print("No data to save.")
            return

        clean_data = []
        timestamp = datetime.now()

        for coin_id, values in raw_data.items():
            record = {
                "ticker": coin_id,
                "price": values["usd"],
                "created_at": timestamp,
            }
            clean_data.append(record)

        if clean_data:
            df = pd.DataFrame(clean_data)
            try:
                df.to_sql("market_prices", self.engine, if_exists="append", index=False)
                print("Data saved successfully.")
            except Exception as e:
                print(f"Error saving data to database: {e}")
