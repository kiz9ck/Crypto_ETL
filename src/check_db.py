import pandas as pd
from sqlalchemy import create_engine
from config import Config


def inspect_db():
    print("--- Inspect Database ---")
    engine = create_engine(Config.DB_URL)

    try:
        query = "SELECT * FROM market_prices ORDER BY created_at DESC LIMIT 10"
        df = pd.read_sql(query, engine)

        if df.empty:
            print("No data found in the database.")
        else:
            print("Latest entries in the database:")
            print(df)

    except Exception as e:
        print(f"Error accessing the database: {e}")


if __name__ == "__main__":
    inspect_db()
