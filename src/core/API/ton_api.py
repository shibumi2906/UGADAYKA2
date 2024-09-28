import pytonlib

class TonAPI:
    def __init__(self, wallet_address, private_key):
        self.wallet_address = wallet_address
        self.private_key = private_key
        self.client = pytonlib.TonlibClient()

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
