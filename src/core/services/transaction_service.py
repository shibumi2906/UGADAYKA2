class TransactionService:
    def __init__(self, ton_api):
        """
        Инициализация сервиса управления транзакциями.
        :param ton_api: Инстанс API для работы с блокчейном TON.
        """
        self.ton_api = ton_api

    def create_transaction(self, user_id, to_address, token_id, amount):
        """
        Создание и отправка транзакции в блокчейн.
        :param user_id: ID пользователя.
        :param to_address: Адрес получателя.
        :param token_id: ID токена.
        :param amount: Сумма транзакции.
        """
        # Отправка транзакции через TON API
        transaction = self.ton_api.send_transaction(to_address, amount)

        # Логика для сохранения транзакции в базе данных или логах
        transaction_record = {
            "user_id": user_id,
            "to_address": to_address,
            "token_id": token_id,
            "amount": amount,
            "status": "pending",
            "transaction_id": transaction["id"]
        }
        # Сохранить transaction_record в базе данных
        return transaction_record

    def check_transaction_status(self, transaction_id):
        """
        Проверка статуса транзакции в блокчейне.
        :param transaction_id: ID транзакции.
        """
        # Взаимодействие с API для получения статуса транзакции
        status = self.ton_api.get_transaction_status(transaction_id)
        return status
