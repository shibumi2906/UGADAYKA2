import pytonlib
import requests
from pathlib import Path


class TonAPI:
    def __init__(self, wallet_address, private_key):
        self.wallet_address = wallet_address
        self.private_key = private_key

        # Скачиваем конфигурацию сети TON (mainnet)
        ton_config = requests.get('https://ton.org/global.config.json').json()

        # Создаем директорию для keystore
        keystore_dir = '/tmp/ton_keystore'  # Путь может быть изменен под нужды ОС
        Path(keystore_dir).mkdir(parents=True, exist_ok=True)

        # Инициализация клиента с параметрами
        self.client = pytonlib.TonlibClient(
            ls_index=0,  # Выбор первого LiteServer
            config=ton_config,
            keystore=keystore_dir
        )

    def get_balance(self):
        """Получение баланса кошелька"""
        try:
            balance = self.client.get_account_balance(self.wallet_address)
            return balance
        except Exception as e:
            print(f"Ошибка при получении баланса: {e}")
            return None

    def send_transaction(self, to_address, amount, message=""):
        """Отправка транзакции"""
        try:
            transaction = self.client.create_transaction(
                private_key=self.private_key,
                to_address=to_address,
                amount=amount,
                message=message
            )
            return transaction
        except Exception as e:
            print(f"Ошибка при отправке транзакции: {e}")
            return None

