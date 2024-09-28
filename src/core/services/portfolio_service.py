class PortfolioService:
    def __init__(self):
        """
        Инициализация сервиса управления портфелем.
        """
        # В качестве примера - используем простой словарь для хранения балансов.
        # В реальной системе это может быть база данных.
        self.portfolios = {}

    def get_balance(self, user_id, token_id):
        """
        Получение баланса пользователя по токену.
        :param user_id: ID пользователя.
        :param token_id: ID токена.
        :return: Баланс токена.
        """
        return self.portfolios.get(user_id, {}).get(token_id, 0)

    def update_balance(self, user_id, token_id, amount):
        """
        Обновление баланса пользователя.
        :param user_id: ID пользователя.
        :param token_id: ID токена.
        :param amount: Сумма для обновления (может быть отрицательной).
        """
        if user_id not in self.portfolios:
            self.portfolios[user_id] = {}

        self.portfolios[user_id][token_id] = self.portfolios[user_id].get(token_id, 0) + amount

    def save_bet(self, user_id, bet_info):
        """
        Сохранение информации о ставке пользователя.
        :param user_id: ID пользователя.
        :param bet_info: Данные о ставке.
        """
        # В реальной системе это может быть сохранение в базу данных
        print(f"Ставка сохранена для пользователя {user_id}: {bet_info}")
