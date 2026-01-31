import requests
from typing import List, Dict, Any


class CryptoFetcher:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def get_prices(self, coins_ids: List[str]) -> Dict[str, Any]:
        ids_string = ",".join(coins_ids)
        params = {"ids": ids_string, "vs_currencies": "usd"}

        try:
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching data from API: {e}")
            return {}
