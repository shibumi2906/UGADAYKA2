import requests

class ExchangeAPI:
    BASE_URL = "https://api.coingecko.com/api/v3"

    @staticmethod
    def get_token_price(token_id, currency="usd"):
        """Получение текущей цены токена в указанной валюте"""
        url = f"{ExchangeAPI.BASE_URL}/simple/price"
        params = {
            "ids": token_id,
            "vs_currencies": currency
        }
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()
            return data[token_id][currency]
        except Exception as e:
            print(f"Ошибка при получении цены токена: {e}")
            return None

    @staticmethod
    def get_market_trends():
        """Получение трендов рынка"""
        url = f"{ExchangeAPI.BASE_URL}/search/trending"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            return data["coins"]
        except Exception as e:
            print(f"Ошибка при получении трендов: {e}")
            return None
